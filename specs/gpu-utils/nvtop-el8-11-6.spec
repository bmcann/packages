Name:           nvtop
Version:        2.0.0
Release:        1%{?dist}
Summary:        Nvidia GPUs htop like monitoring tool

Group:          Applications/System
License:        GPLv3+
URL:            https://github.com/Syllo/nvtop
Source0:        %{name}-%{version}.tar.gz

Vendor:         Maxime Schmitt (@Syllo on GitHub)
Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>

BuildArch:      x86_64

BuildRequires:  cmake ncurses-devel
Requires:       ncurses nvidia-driver-NVML

%description
Nvtop stands for Neat Videocard TOP, a (h)top like task monitor for AMD and
Nvidia GPUs. It can handle multiple GPUs and print information about them in a
htop familiar way.

This package was built on Rocky Linux 8 with CUDA 11.6 but without support for
AMD GPUs enabled.

%prep
%setup -q

%build
%{__mkdir} build
cd build
module load cuda/11.6
%cmake .. -DNVIDIA_SUPPORT=ON -DAMDGPU_SUPPORT=OFF
make %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_bindir}
%{__mkdir} -p %{buildroot}%{_mandir}/man1
%{__install} -m 755 build/src/nvtop %{buildroot}%{_bindir}/
%{__install} -m 644 build/manpage/nvtop %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/nvtop
%doc %{_mandir}/man1/nvtop.gz

%changelog
* Thu Apr  7 2022 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 2.0.0
- Package nvtop for Rocky Linux 8 and CUDA 11.6

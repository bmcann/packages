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

BuildRequires:  cmake3 ncurses-devel
Requires:       ncurses nvidia-driver-latest-dkms-NVML

%description
Nvtop stands for Neat Videocard TOP, a (h)top like task monitor for AMD and
Nvidia GPUs. It can handle multiple GPUs and print information about them in a
htop familiar way.

This package was built on CentOS 7 with CUDA 10.2 but without support for AMD
GPUs enabled.

%prep
%setup -q

%build
%{__mkdir} build
cd build
module load cuda/10.2
%cmake3 .. -DNVIDIA_SUPPORT=ON -DAMDGPU_SUPPORT=OFF
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
- Package nvtop for CentOS 7 and CUDA 10.2

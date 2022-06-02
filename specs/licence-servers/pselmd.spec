%define tarball FLEXlm

Name:           pselmd
Version:        11.16.3.0
Release:        2%{?dist}
Summary:        The PSE gPROMS licence manager

License:        Commercial
Group:          System Environment/Daemons
URL:            https://www.psenterprise.com
Source0:        %{tarball}-%{vendor}-%{version}-x64_lsb.tgz

Vendor:         PSE
Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>

BuildArch:      x86_64

BuildRoot:      %{_tmppath}/%{tarball}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  coreutils
Requires:       flexlm = 11.16.3.0, systemd

%description
This package installs the PSE gPROMS licence manager daemon (PSELMD).

%prep
%setup -q -n %{tarball}-%{vendor}-%{version}-x64_lsb
%{__rm} -f FLEXlm.init
%{__rm} -f FLEXlm.conf
%{__rm} -f bin/lmgrd
%{__rm} -f bin/lmutil
%{__rm} -rf licenses
%{__rm} -rf log

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{_sharedstatedir}/FLEXlm/bin
%{__install} -m 755 bin/PSELMD %{buildroot}/%{_sharedstatedir}/FLEXlm/bin/

%clean
rm -rf %{buildroot}

%preun
if [ "$1" = "0" ]; then
    /usr/bin/systemctl stop lmgrd@PSELMD.service > /dev/null 2>&1
fi

%files
%defattr(-,root,root,-)
%{_sharedstatedir}/FLEXlm/bin/PSELMD

%changelog
* Fri Apr  1 2022 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 11.16.3.0
- Repackage PSELMD to bump the release number as the updated systemd unit file
  in the FLEXlm RPM bumped the release number of that package and we want to
  keep the version numbers of both packages the same

* Mon Feb  8 2021 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 11.16.3.0
- Package PSELMD for CentOS 7

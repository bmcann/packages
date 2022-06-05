%define tarball FLEXlm

Name:           chemcompd
Version:        11.17.1.0
Release:        2%{?dist}
Summary:        The CCG MOE licence manager

License:        Commercial
Group:          System Environment/Daemons
URL:            https://www.chemcomp.com
Source0:        moe_2020_license_manager_11.17.1.tgz

Vendor:         Chemical Computing Group
Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>

BuildArch:      x86_64

BuildRequires:  coreutils
Requires:       flexlm = 11.17.1.0, systemd

%description
This package installs the CCG MOE licence manager daemon (chemcompd).

%prep
%setup -q -c moe_2020_license_manager_11.17.1
%{__rm} -rf bin
%{__rm} -f bin/bin-lnx64/lmgrd
%{__rm} -f bin/bin-lnx64/lmutil
%{__rm} -rf bin/bin-mac64
%{__rm} -rf bin/bin-win64
%{__rm} -rf html
%{__rm} -f chemcomp-licadmin.service.cfg
%{__rm} -f license.dat
%{__rm} -f lm_version.txt
%{__rm} -f moe2020_standalone_license_manager_guide.htm

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{_sharedstatedir}/FLEXlm/bin
%{__install} -m 755 bin-lnx64/chemcompd %{buildroot}/%{_sharedstatedir}/FLEXlm/bin/

%clean
rm -rf %{buildroot}

%preun
if [ "$1" = "0" ]; then
    /usr/bin/systemctl stop lmgrd@chemcompd.service > /dev/null 2>&1
fi

%files
%defattr(-,root,root,-)
%{_sharedstatedir}/FLEXlm/bin/chemcompd

%changelog
* Fri Apr  1 2022 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 11.17.1.0
- Repackage chemcompd to bump the release number as the updated systemd unit
  file in the FLEXlm RPM bumped the release number of that package and we want
  to keep the version numbers of both packages the same

* Tue Jun 15 2021 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 11.17.1.0
- Package chemcompd for CentOS 7

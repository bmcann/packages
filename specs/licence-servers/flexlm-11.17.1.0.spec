%define tarball FLEXlm

Name:           flexlm
Version:        11.17.1.0
Release:        2%{?dist}
Summary:        The FLEXlm licence manager

License:        Commercial
Group:          System Environment/Daemons
URL:            https://www.flexerasoftware.com
Source0:        moe_2020_license_manager_11.17.1.tgz
Source1:        lmgrd@.service

Vendor:         Chemical Computing Group
Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>

BuildArch:      x86_64

BuildRoot:      %{_tmppath}/%{tarball}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  coreutils, sed, systemd, systemd-rpm-macros
Requires:       coreutils, redhat-lsb-core, shadow-utils, systemd

%description
This package installs the FLEXlm licence manager daemon (lmgrd).

%prep
%setup -q -c moe_2020_license_manager_11.17.1
%{__rm} -rf bin
%{__rm} -f bin/bin-lnx64/chemcompd
%{__rm} -rf bin/bin-mac64
%{__rm} -rf bin/bin-win64
%{__rm} -rf html
%{__rm} -f chemcomp-licadmin.service.cfg
%{__rm} -f license.dat
%{__rm} -f lm_version.txt
%{__rm} -f moe2020_standalone_license_manager_guide.htm
%{__cat} << 'EOF' > FLEXlm.conf
# Space-separated list of vendor daemons to start
# The licence and log files will be derived from these names
# NOTE: This file is no longer used since moving to systemd service management
FLEXLM_VENDORS=""
EOF
%{__cp} -a %{SOURCE1} ./

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{_sysconfdir}/sysconfig
%{__mkdir} -p %{buildroot}/%{_unitdir}
%{__mkdir} -p %{buildroot}/%{_sharedstatedir}/FLEXlm/bin
%{__mkdir} -p %{buildroot}/%{_sharedstatedir}/FLEXlm/licences
%{__mkdir} -p %{buildroot}/%{_localstatedir}/log/FLEXlm
%{__install} -m 644 FLEXlm.conf %{buildroot}/%{_sysconfdir}/sysconfig/FLEXlm
%{__install} -m 644 lmgrd@.service %{buildroot}/%{_unitdir}/
%{__install} -m 755 bin-lnx64/lmgrd %{buildroot}/%{_sharedstatedir}/FLEXlm/bin/
%{__install} -m 755 bin-lnx64/lmutil %{buildroot}/%{_sharedstatedir}/FLEXlm/bin/

%clean
rm -rf %{buildroot}

%preun
if [ "$1" = "0" ]; then
    /usr/bin/systemctl stop lmgrd\@*.service > /dev/null 2>&1
fi

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/sysconfig/FLEXlm
%{_unitdir}/lmgrd@.service
%{_sharedstatedir}/FLEXlm/bin/lmgrd
%{_sharedstatedir}/FLEXlm/bin/lmutil
%dir %{_sharedstatedir}/FLEXlm/licences
%dir %{_localstatedir}/log/FLEXlm

%changelog
* Fri Apr  1 2022 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 11.17.1.0
- Repackage lmgrd and lmutil with updated systemd unit file

* Tue Jun 15 2021 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 11.17.1.0
- Package lmgrd and lmutil for CentOS 7

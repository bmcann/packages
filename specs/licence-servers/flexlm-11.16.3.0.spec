%define tarball FLEXlm

Name:           flexlm
Version:        11.16.3.0
Release:        2%{?dist}
Summary:        The FLEXlm licence manager

License:        Commercial
Group:          System Environment/Daemons
URL:            https://www.flexerasoftware.com
Source0:        %{tarball}-%{vendor}-%{version}-x64_lsb.tgz
Source1:        lmgrd@.service

Vendor:         PSE
Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>

BuildArch:      x86_64

BuildRequires:  coreutils, sed, systemd, systemd-rpm-macros
Requires:       coreutils, redhat-lsb-core, shadow-utils, systemd

%description
This package installs the FLEXlm licence manager daemon (lmgrd).

%prep
%setup -q -n %{tarball}-%{vendor}-%{version}-x64_lsb
%{__rm} -f bin/PSELMD
%{__rm} -f FLEXlm.init
%{__rm} -f FLEXlm.conf
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
%{__install} -m 755 bin/lmgrd %{buildroot}/%{_sharedstatedir}/FLEXlm/bin/
%{__install} -m 755 bin/lmutil %{buildroot}/%{_sharedstatedir}/FLEXlm/bin/

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
* Fri Apr  1 2022 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 11.16.3.0
- Repackage lmgrd and lmutil with updated systemd unit file

* Mon Feb  8 2021 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 11.16.3.0
- Package lmgrd and lmutil for CentOS 7

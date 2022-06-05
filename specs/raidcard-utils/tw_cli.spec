Name:           tw_cli
Version:        2.00.11.022
Release:        1
Summary:        CLI utility for 3ware RAID cards

License:        LSI Corporation
Group:          System Environment/Base
URL:            https://dl.dell.com/FOLDER06239763M/1/mvcli_5.0.13.1107_A06.zip
Source0:        %{name}-%{version}.tar.gz

Vendor:         3ware
Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>

BuildArch:      x86_64

%description
A command line interface utility for 3ware RAID cards, release 10.2 supports the
9750, 9690SA and 9650SE models

%prep
%setup -q -n %{name}-%{version}

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{_sbindir}
%{__mkdir} -p %{buildroot}/%{_mandir}/man8
%{__install} -m 750 tw_cli %{buildroot}/%{_sbindir}/
%{__install} -m 644 tw_cli.8.nroff %{buildroot}/%{_mandir}/man8/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/tw_cli
%{_mandir}/man8/tw_cli.8.nroff.gz

%changelog
* Tue Nov  3 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 2.00.11.022
- Package tw_cli for CentOS

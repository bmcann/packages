Name:           perccli
Version:        007.1020.0000.0000
Release:        1
Summary:        CLI utility for Dell PERC cards

License:        AVAGO Technologies
Group:          System Environment/Base
URL:            http://www.avagotech.com
Source0:        %{name}-%{version}.tar.gz

Vendor:         AVAGO Technologies
Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>

BuildArch:      x86_64

%description
A command line interface utility for Dell PowerEdge RAID Controller cards

%prep
%setup -q -n %{name}-%{version}

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{_sbindir}
%{__install} -m 750 perccli64 %{buildroot}/%{_sbindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/perccli64

%changelog
* Mon Sep 21 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 007.1020.0000.0000
- Package perccli64 for CentOS

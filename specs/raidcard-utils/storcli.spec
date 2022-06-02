Name:           storcli
Version:        007.1416.0000.0000
Release:        1
Summary:        CLI utility for LSI RAID cards

License:        Broadcom Inc.
Group:          System Environment/Base
URL:            http://www.broadcom.com
Source0:        %{name}-%{version}.tar.gz

Vendor:         Broadcom Inc.
Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>

BuildArch:      x86_64

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A command line interface utility for LSI RAID controller cards

%prep
%setup -q -n %{name}-%{version}

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{_sbindir}
%{__install} -m 750 storcli64 %{buildroot}/%{_sbindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/storcli64

%changelog
* Mon Sep 21 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 007.1416.0000.0000
- Package storcli64 for CentOS

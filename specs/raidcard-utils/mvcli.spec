Name:           mvcli
Version:        5.0.13.1107
Release:        A06
Summary:        CLI utility for Dell BOSS-S1 cards

License:        Dell Software License Agreement
Group:          System Environment/Base
URL:            https://dl.dell.com/FOLDER06239763M/1/mvcli_5.0.13.1107_A06.zip
Source0:        %{name}-%{version}.tar.gz

Vendor:         Dell
Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>

BuildArch:      x86_64

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A command line interface utility for Dell Boot Optimised Storage Solution BOSS-S1 cards

%prep
%setup -q -n %{name}-%{version}

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{_sbindir}
%{__mkdir} -p %{buildroot}/%{_libdir}
%{__install} -m 750 mvcli %{buildroot}/%{_sbindir}/
%{__install} -m 755 libmvraid.so %{buildroot}/%{_libdir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/mvcli
%{_libdir}/libmvraid.so

%changelog
* Mon Sep 21 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 5.0.13.1107
- Package mvcli and libmvraid for CentOS

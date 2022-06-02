Name:           orglab
Version:        11.16.5.1
Release:        1%{?dist}
Summary:        The Origin licence manager

License:        Commercial
Group:          System Environment/Daemons
URL:            https://www.originlab.com
Source0:        %{name}.zip

Vendor:         OriginLab
Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>

BuildArch:      i686

BuildRoot:      %{_tmppath}/%{tarball}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  coreutils
Requires:       flexlm = 11.16.5.1, systemd

%description
This package installs the 32-bit Origin licence manager daemon (orglab).

%prep
%{__rm} -rf %{_topdir}/BUILD/%{name}
unzip %{SOURCE0}

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{_sharedstatedir}/FLEXlm/bin
%{__install} -m 755 orglab %{buildroot}/%{_sharedstatedir}/FLEXlm/bin/

%clean
rm -rf %{buildroot}

%preun
if [ "$1" = "0" ]; then
    /usr/bin/systemctl stop lmgrd@orglab.service > /dev/null 2>&1
fi

%files
%defattr(-,root,root,-)
%{_sharedstatedir}/FLEXlm/bin/orglab

%changelog
* Tue Feb 22 2022 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 11.16.5.1
- Package orglab for CentOS 7 and i686 architecture

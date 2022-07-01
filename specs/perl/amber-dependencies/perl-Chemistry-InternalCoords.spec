# $Id: perl-Chemistry-InternalCoords.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-InternalCoords

Name:           perl-Chemistry-InternalCoords
Version:        0.18
Release:        1%{?dist}
Summary:        Represent the position of an atom using internal coordinates and convert it to Cartesian coordinates
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-InternalCoords

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-InternalCoords-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::Bond::Find) >= 0.2
Requires:       perl(Chemistry::Canonicalize) >= 0.1
Requires:       perl(Chemistry::Mol) >= 0.25
Requires:       perl(Scalar::Util)

%description
This module implements an object class for representing internal coordinates
and provides methods for converting them to Cartesian coordinates. For
generating an internal coordinate representation (aka a Z-matrix) of a molecule
from its Cartesian coordinates, see the Chemistry::InternalCoords::Builder module.
This module is part of the PerlMol project; http://www.perlmol.org/.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644, root, root, 0755)
%doc Changes README META.yml MYMETA.json MYMETA.yml
%doc %{_mandir}/man3/Chemistry::InternalCoords.3pm*
%doc %{_mandir}/man3/Chemistry::InternalCoords::Builder.3pm*
%dir %{perl_vendorlib}/Chemistry/InternalCoords/
%{perl_vendorlib}/Chemistry/InternalCoords.pm
%{perl_vendorlib}/Chemistry/InternalCoords/Builder.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.18-1
- Initial package.

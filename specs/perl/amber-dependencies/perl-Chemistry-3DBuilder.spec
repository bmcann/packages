# $Id: perl-Chemistry-3DBuilder.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-3DBuilder

Name:           perl-Chemistry-3DBuilder
Version:        0.10
Release:        1%{?dist}
Summary:        Generate 3D coordinates from a connection table
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-3DBuilder

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-3DBuilder-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::File::SMARTS) >= 0.21
Requires:       perl(Chemistry::File::SMILES) >= 0.43
Requires:       perl(Chemistry::InternalCoords) >= 0.18
Requires:       perl(Chemistry::Mol) >= 0.33
Requires:       perl(Chemistry::Pattern) >= 0.25
Requires:       perl(Chemistry::Ring) >= 0.18
Requires:       perl(Math::VectorReal) >= 1.00

%description
This module generates a three-dimensional molecular structure from a connection
table, such as that obtained by a 2D representation of the molecule or from a
SMILES string. NOTE: this module is still at a very early stage of development
so it has important limitations. 1) It doesn't handle rings or stereochemistry
yet! 2) The bond lengths and atoms are very approximate as they don't really
account for different elements. 3) Only the sp3, sp2, and sp hybridizations are
supported. This module is part of the PerlMol project; http://www.perlmol.org/.

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
%doc %{_mandir}/man3/Chemistry::3DBuilder.3pm*
%dir %{perl_vendorlib}/Chemistry/
%{perl_vendorlib}/Chemistry/3DBuilder.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.10-1
- Initial package.

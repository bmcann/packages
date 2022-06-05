# $Id: perl-Chemistry-MacroMol.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-MacroMol

Name:           perl-Chemistry-MacroMol
Version:        0.06
Release:        1%{?dist}
Summary:        Perl module for macromolecules
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-MacroMol

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-MacroMol-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::Mol) >= 0.24
Requires:       perl(Scalar::Util)

%description
For the purposes of this module, a macromolecule is just a molecule that
consists of several "domains". For example, a protein consists of aminoacid
residues, or a nucleic acid consists of bases. Therefore Chemistry::MacroMol
is derived from Chemistry::Mol, with additional methods to handle the domains.
The way things are currently structured, an atom in a macromolecule "belong"
both to the MacroMol object and to a Domain object. This way you can get all the
atoms in $protein via $protein->atoms, or to the atoms in residue 123 via
$protein->domain(123)->atoms.
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
%doc Changes README MYMETA.json MYMETA.yml
%doc %{_mandir}/man3/Chemistry::Domain.3pm*
%doc %{_mandir}/man3/Chemistry::MacroMol.3pm*
%dir %{perl_vendorlib}/Chemistry/
%{perl_vendorlib}/Chemistry/Domain.pm
%{perl_vendorlib}/Chemistry/MacroMol.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.06-1
- Initial package.

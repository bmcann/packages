# $Id: perl-Chemistry-FormulaPattern.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-FormulaPattern

Name:           perl-Chemistry-FormulaPattern
Version:        0.10
Release:        1%{?dist}
Summary:        Match molecule by formula
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-FormulaPattern

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-FormulaPattern-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::Mol) >= 0.24
Requires:       perl(Chemistry::Pattern) >= 0.20
Requires:       perl(Test::More)
Requires:       perl(Text::Balanced)

%description
This module implements a simple language for describing a range of molecular
formulas and allows one to find out whether a molecule matches the formula
specification. It can be used for searching for molecules by formula, in a way
similar to the NIST WebBook formula search
(http://webbook.nist.gov/chemistry/form-ser.html). Note however that the
language used by this module is different from the one used by the WebBook!
Chemistry::FormulaPattern shares the same interface as Chemistry::Pattern.
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
%doc %{_mandir}/man3/Chemistry::FormulaPattern.3pm*
%doc %{_mandir}/man3/Chemistry::File::FormulaPattern.3pm*
%dir %{perl_vendorlib}/Chemistry/File/
%{perl_vendorlib}/Chemistry/FormulaPattern.pm
%{perl_vendorlib}/Chemistry/File/FormulaPattern.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.10-1
- Initial package.

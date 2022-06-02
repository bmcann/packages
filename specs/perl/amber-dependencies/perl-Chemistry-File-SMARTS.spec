# $Id: perl-Chemistry-File-SMARTS.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-File-SMARTS

Name:           perl-Chemistry-File-SMARTS
Version:        0.22
Release:        1%{?dist}
Summary:        SMARTS chemical substructure pattern linear notation parser
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-File-SMARTS

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-File-SMARTS-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::File::SMILES) >= 0.41
Requires:       perl(Chemistry::Pattern) >= 0.25
Requires:       perl(Chemistry::Mol) >= 0.24
Requires:       perl(Chemistry::Ring) >= 0.16
Requires:       perl(List::Util)
Requires:       perl(Test::More)

%description
This module parses a SMARTS (SMiles ARbitrary Target Specification) string,
generating a Chemistry::Pattern object. It is a file I/O driver for the PerlMol
toolkit; http://www.perlmol.org. It is not called directly but by means of the
Chemistry::Pattern->parse class method. For a detailed description of the SMARTS
language, see http://www.daylight.com/dayhtml/doc/theory/theory.smarts.html.
Note that this module doesn't implement the full language, as detailed under
CAVEATS.

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
%doc %{_mandir}/man3/Chemistry::File::SMARTS.3pm*
%dir %{perl_vendorlib}/Chemistry/File/
%{perl_vendorlib}/Chemistry/File/SMARTS.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.22-1
- Initial package.

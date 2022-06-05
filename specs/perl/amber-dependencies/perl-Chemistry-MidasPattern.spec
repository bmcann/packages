# $Id: perl-Chemistry-MidasPattern.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-MidasPattern

Name:           perl-Chemistry-MidasPattern
Version:        0.11
Release:        1%{?dist}
Summary:        Select atoms in macromolecules
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-MidasPattern

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-MidasPattern-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::File::PDB) >= 0.21
Requires:       perl(Chemistry::MacroMol) >= 0.05
Requires:       perl(Chemistry::Mol) >= 0.24
Requires:       perl(Chemistry::Pattern) >= 0.20
Requires:       perl(Test::Simple)

%description
This module partially implements a pattern matching engine for selecting atoms
in macromolecules by using Midas/Chimera patterns. See
http://www.cmpharm.ucsf.edu/~troyer/troff2html/midas/Midas-uh-3.html#sh-2.1 for
a detailed description of this language. This module shares the same interface
as Chemistry::Pattern.
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
%doc %{_mandir}/man3/Chemistry::MidasPattern.3pm*
%doc %{_mandir}/man3/Chemistry::File::MidasPattern.3pm*
%dir %{perl_vendorlib}/Chemistry/File/
%{perl_vendorlib}/Chemistry/MidasPattern.pm
%{perl_vendorlib}/Chemistry/File/MidasPattern.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.11-1
- Initial package.

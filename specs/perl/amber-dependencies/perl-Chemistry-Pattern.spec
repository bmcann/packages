# $Id: perl-Chemistry-Pattern.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-Pattern

Name:           perl-Chemistry-Pattern
Version:        0.27
Release:        1%{?dist}
Summary:        Chemical substructure pattern matching
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-Pattern

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-Pattern-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::Mol) >= 0.24
Requires:       perl(Test::Simple)

%description
This module implements basic pattern matching for molecules. The
Chemistry::Pattern class is a subclass of Chemistry::Mol, so patterns have all
the properties of molecules and can come from reading the same file formats. Of
course there are certain formats (such as SMARTS) that are exclusively used to
describe patterns.
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
%doc %{_mandir}/man3/Chemistry::Pattern.3pm*
%doc %{_mandir}/man3/Chemistry::Pattern::Atom.3pm*
%doc %{_mandir}/man3/Chemistry::Pattern::Bond.3pm*
%dir %{perl_vendorlib}/Chemistry/Pattern/
%{perl_vendorlib}/Chemistry/Pattern.pm
%{perl_vendorlib}/Chemistry/Pattern/Atom.pm
%{perl_vendorlib}/Chemistry/Pattern/Bond.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.27-1
- Initial package.

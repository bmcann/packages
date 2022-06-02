# $Id: perl-Chemistry-Mok.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-Mok

Name:           perl-Chemistry-Mok
Version:        0.25
Release:        1%{?dist}
Summary:        Molecular awk interpreter
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-Mok

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-Mok-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::3DBuilder) >= 0.1
Requires:       perl(Chemistry::Bond::Find) >= 0.21
Requires:       perl(Chemistry::File::SMARTS) >= 0.11
Requires:       perl(Chemistry::Isotope) >= 0.1
Requires:       perl(Chemistry::Mol) >= 0.3
Requires:       perl(Chemistry::Pattern) >= 0.21
Requires:       perl(Math::VectorReal) >= 1
Requires:       perl(Scalar::Util) >= 1.01
Requires:       perl(Test::Simple)
Requires:       perl(Text::Balanced) >= 1.87

%description
This module is the engine behind the mok program. See mok(1) for a detailed
description of the language.
Mok is part of the PerlMol project; http://www.perlmol.org/.

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
%doc %{_mandir}/man1/mok.1*
%doc %{_mandir}/man3/Chemistry::Mok.3pm*
%dir %{perl_vendorlib}/Chemistry/
%{perl_vendorlib}/Chemistry/Mok.pm
%attr(0755, root, root) %{_bindir}/mok

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.25-1
- Initial package.

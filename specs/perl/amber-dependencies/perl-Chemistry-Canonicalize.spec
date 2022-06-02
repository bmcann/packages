# $Id: perl-Chemistry-Canonicalize.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-Canonicalize

Name:           perl-Chemistry-Canonicalize
Version:        0.11
Release:        1%{?dist}
Summary:        Number the atoms in a molecule in a unique way
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-Canonicalize

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-Canonicalize-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::Mol) >= 0.24
Requires:       perl(Math::BigInt)

%description
This module provides functions for "canonicalizing" a molecular structure;
that is, to number the atoms in a unique way regardless of the input order.
The canonicalization algorithm is based on:
Weininger, et. al., J. Chem. Inf. Comp. Sci. 29[2], 97-101 (1989)
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
%doc %{_mandir}/man3/Chemistry::Canonicalize.3pm*
%dir %{perl_vendorlib}/Chemistry/
%{perl_vendorlib}/Chemistry/Canonicalize.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.11-1
- Initial package.

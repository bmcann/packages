# $Id: perl-Chemistry-Reaction.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-Reaction

Name:           perl-Chemistry-Reaction
Version:        0.02
Release:        1%{?dist}
Summary:        Explicit chemical reactions
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-Reaction

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-Reaction-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

Patch0:         Chemistry-Reaction-%{version}.patch

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::File::SMILES) >= 0.42
Requires:       perl(Chemistry::Mol) >= 0.26
Requires:       perl(Chemistry::Pattern) >= 0.25

%description
This package, along with Chemistry::Pattern, provides an implementation of
explicit chemical reactions. An explicit chemical reaction is a representation
of the transformation that takes place in a given chemical reaction. In an
explicit chemical reaction, a substrate molecule is transformed into a product
molecule by breaking existing bonds and creating new bonds between atoms. The
representation of an explicit chemical reaction is a molecule in which the
order of a bond before the chemical reaction is distinguished from the order of
the bond after the chemical reaction.
This module is part of the PerlMol project; http://www.perlmol.org/.

%prep
%setup -n %{real_name}-%{version}
%patch0

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
%doc %{_mandir}/man3/Chemistry::Reaction.3pm*
%dir %{perl_vendorlib}/Chemistry/
%{perl_vendorlib}/Chemistry/Reaction.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.02-1
- Initial package.

# $Id: perl-Chemistry-Mol.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-Mol

Name:           perl-Chemistry-Mol
Version:        0.38
Release:        1%{?dist}
Summary:        Molecule object toolkit
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-Mol

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Andrius Merkys <andrius.merkys@gmail.com>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-Mol-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Math::VectorReal) >= 1.0
Requires:       perl(IO::String)
Requires:       perl(Scalar::Util) >= 1.01
Requires:       perl(Test::Simple)
Requires:       perl(Text::Balanced)
Recommends:     perl(Chemistry::InternalCoords)
Recommends:     perl(Chemistry::Isotope)
Recommends:     perl(Compress::Zlib)

%description
This toolkit includes basic objects and methods to describe molecules. It
consists of several modules: Chemistry::Mol, Chemistry::Atom,
Chemistry::Bond, and Chemistry::File. These are the core modules of the
PerlMol toolkit; see http://www.perlmol.org/.

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
%doc Changes README META.yml MYMETA.yml MYMETA.json
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Chemistry/
%{perl_vendorlib}/Chemistry/*.pm
%{perl_vendorlib}/Chemistry/File/
%{perl_vendorlib}/Chemistry/Tutorial.pod

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.38-1
- Rebuilt for CentOS 7

* Thu Jul 16 2009 Christoph Maser <cmr@financial.com> - 0.37-1
- Updated to version 0.37.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.36-1
- Updated to release 0.36.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.35-1
- Updated to release 0.35.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.32-1
- Updated to release 0.32.

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Initial package.

# $Id: perl-Chemistry-File-MDLMol.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-File-MDLMol

Name:           perl-Chemistry-File-MDLMol
Version:        0.24
Release:        1%{?dist}
Summary:        MDL molfile reader/writer
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-File-MDLMol

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Andrius Merkys <andrius.merkys@gmail.com>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-File-MDLMol-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(Chemistry::Mol) >= 0.35
Recommends:     perl(Chemistry::Isotope)
Recommends:     perl(Chemistry::Ring) >= 0.19
Recommends:     perl(Chemistry::Pattern)

%description
MDL Molfile (V2000) reader/writer. This module automatically registers the
'mdl' format with Chemistry::Mol. The first three lines of the molfile are
stored as $mol->name, $mol->attr("mdlmol/line2"), and
$mol->attr("mdlmol/comment").
This version only reads and writes some of the information available in a
molfile: it reads coordinats, atom and bond types, charges, radicals and atom
lists. It does not read other things such as stereochemistry, 3d properties,
isotopes, etc.
This module is part of the PerlMol project; http://www.perlmol.org.

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
%doc %{_mandir}/man3/Chemistry::File::MDLMol.3pm*
%doc %{_mandir}/man3/Chemistry::File::SDF.3pm*
%dir %{perl_vendorlib}/Chemistry/File/
%{perl_vendorlib}/Chemistry/File/MDLMol.pm
%{perl_vendorlib}/Chemistry/File/SDF.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.21-1
- Initial package.

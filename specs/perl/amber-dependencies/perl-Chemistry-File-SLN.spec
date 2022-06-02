# $Id: perl-Chemistry-File-SLN.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-File-SLN

Name:           perl-Chemistry-File-SLN
Version:        0.11
Release:        1%{?dist}
Summary:        SLN linear notation parser/writer
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-File-SLN

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-File-SLN-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::Bond::Find) >= 0.21
Requires:       perl(Chemistry::Canonicalize) >= 0.10
Requires:       perl(Chemistry::Mol) >= 0.26
Requires:       perl(Chemistry::Ring) >= 0.15
Requires:       perl(List::Util)
Requires:       perl(Parse::Yapp)
Requires:       perl(Test::More)

%description
This module parses a SLN (Sybyl Line Notation) string.
This is a File I/O driver for the PerlMol project. http://www.perlmol.org/. It
registers the 'sln' format with Chemistry::Mol, and recognizes filenames ending
in '.sln'. Optional attributes for atoms, bonds and molecules are stored as
$atom->attr("sln/attr"), $bond->attr("sln/attr"), and $mol->attr("sln/attr"),
respectively. Boolean attributes are stored with a value of 'TRUE'. That's the
way boolean attributes are recognized when writing, so that they can be written
in the shortened form.

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
%doc %{_mandir}/man3/Chemistry::File::SLN.3pm*
%dir %{perl_vendorlib}/Chemistry/File/SLN/
%{perl_vendorlib}/Chemistry/File/SLN.pm
%{perl_vendorlib}/Chemistry/File/SLN/Parser.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.11-1
- Initial package.

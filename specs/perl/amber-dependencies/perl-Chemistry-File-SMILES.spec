# $Id: perl-Chemistry-File-SMILES.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-File-SMILES

Name:           perl-Chemistry-File-SMILES
Version:        0.47
Release:        1%{?dist}
Summary:        SMILES linear notation parser/writer
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-File-SMILES

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-File-SMILES-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

Patch0:         Chemistry-File-SMILES-%{version}.patch

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::Bond::Find) >= 0.21
Requires:       perl(Chemistry::Canonicalize) >= 0.10
Requires:       perl(Chemistry::Mol) >= 0.30
Requires:       perl(Chemistry::Ring) >= 0.15
Requires:       perl(List::Util)

%description
This module parses a SMILES (Simplified Molecular Input Line Entry
Specification) string. This is a File I/O driver for the PerlMol project;
http://www.perlmol.org/. It registers the 'smiles' format with Chemistry::Mol.

%prep
%setup -n %{real_name}-%{version}
%patch0
mkdir examples
mv *.txt examples

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
%doc Changes README META.yml MYMETA.json MYMETA.yml TODO examples/
%doc %{_mandir}/man3/Chemistry::File::SMILES.3pm*
%dir %{perl_vendorlib}/Chemistry/File/
%{perl_vendorlib}/Chemistry/File/SMILES.pm
%{perl_vendorlib}/Chemistry/File/write.pl

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.47-1
- Initial package.

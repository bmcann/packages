# $Id: perl-Chemistry-File-PDB.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-File-PDB

Name:           perl-Chemistry-File-PDB
Version:        0.23
Release:        1%{?dist}
Summary:        Protein Data Bank file format reader/writer
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-File-PDB

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-File-PDB-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::MacroMol) >= 0.05
Requires:       perl(Chemistry::Mol) >= 0.30

%description
This module reads and writes PDB files. The PDB file format is commonly used to
describe proteins, particularly those stored in the Protein Data Bank
(http://www.rcsb.org/pdb/). The current version of this module only reads the
following record types, ignoring everything else: ATOM, HETATM, ENDMDL and END.
This module automatically registers the 'pdb' format with Chemistry::Mol, so
that PDB files may be identified and read by Chemistry::Mol->read(). For
autodetection purposes, it assumes that files ending in .pdb or having a line
matching /^(ATOM |HETATM)/ are PDB files. The PDB reader and writer is designed
for dealing with Chemistry::MacroMol objects, but it can also create and use
Chemistry::Mol objects by throwing some information away.
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
%doc %{_mandir}/man3/Chemistry::File::PDB.3pm*
%dir %{perl_vendorlib}/Chemistry/File/
%{perl_vendorlib}/Chemistry/File/PDB.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.23-1
- Initial package.

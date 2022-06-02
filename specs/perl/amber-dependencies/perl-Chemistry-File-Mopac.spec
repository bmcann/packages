# $Id: perl-Chemistry-File-Mopac.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-File-Mopac

Name:           perl-Chemistry-File-Mopac
Version:        0.15
Release:        1%{?dist}
Summary:        MOPAC 6 input file reader/writer
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-File-Mopac

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-File-Mopac-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::InternalCoords) >= 0.15
Requires:       perl(Chemistry::Mol) >= 0.25
Requires:       perl(List::Util)

%description
This module reads and writes MOPAC 6 input files. It can handle both internal
coordinates and cartesian coordinates. It also extracts molecules from summary
files, defined as those files that match /SUMMARY OF/ in the third line. Perhaps
a future version will extract additional information such as the energy and
dipole from the summary file.
This module registers the mop format with Chemistry::Mol. For detection
purposes, it assumes that filenames ending in .mop or .zt have the Mopac format,
as well as files whose first line matches /am1|pm3|mndo|mdg|pdg/i (this may
change in the future).
When the module reads an input file into $mol, it puts the keywords (usually
the first line of the file) in $mol->attr("mopac/keywords"), the comments
(usually everything else on the first three lines) in
$mol->attr("mopac/comments") and $mol->name, and the internal coordinates for
each atom in $atom->internal_coords.
When writing, the kind of coordinates used depend on the coords option, as shown
in the SYNOPSIS. Internal coordinates are used by default. If the molecule has
no internal coordinates defined or the rebuild option is set, the build_zmat
function from Chemistry::InternalCoords::Builder is used to renumber the atoms
and build the Z-matrix from scratch.
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
%doc Changes README MYMETA.json MYMETA.yml
%doc %{_mandir}/man3/Chemistry::File::Mopac.3pm*
%dir %{perl_vendorlib}/Chemistry/File/
%{perl_vendorlib}/Chemistry/File/Mopac.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.15-1
- Initial package.

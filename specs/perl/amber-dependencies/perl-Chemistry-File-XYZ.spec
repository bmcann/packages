# $Id: perl-Chemistry-File-XYZ.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-File-XYZ

Name:           perl-Chemistry-File-XYZ
Version:        0.11
Release:        1%{?dist}
Summary:        XYZ molecule format reader/writer
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-File-XYZ

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-File-XYZ-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::Mol) >= 0.24

%description
This module reads XYZ files. It automatically registers the 'xyz' format with
Chemistry::Mol, so that XYZ files may be identified and read by
Chemistry::Mol->read().
The XYZ format is not strictly defined and there are various versions floating
around; this module accepts the following:
First line: atom count (optional)
Second line: molecule name or comment (optional)
All other lines: (symbol or atomic number), x, y, and z coordinates separated by
spaces, tabs, or commas.
If the first line doesn't look like a number, the atom count is deduced from the
number of lines in the file. If the second line looks like it defines an atom,
it is assumed that there was no name or comment.
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
%doc Changes README MYMETA.json MYMETA.yml
%doc %{_mandir}/man3/Chemistry::File::XYZ.3pm*
%dir %{perl_vendorlib}/Chemistry/File/
%{perl_vendorlib}/Chemistry/File/XYZ.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.11-1
- Initial package.

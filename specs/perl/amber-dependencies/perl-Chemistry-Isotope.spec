# $Id: perl-Chemistry-Isotope.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-Isotope

Name:           perl-Chemistry-Isotope
Version:        0.11
Release:        1%{?dist}
Summary:        Table of the isotopes exact mass data
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-Isotope

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-Isotope-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Test::Simple)

%description
This module contains the exact mass data from the table of the isotopes. It has
an exportable function, isotope_mass, which returns the mass of an atom in mass
units given its mass number (A) and atomic number (Z); and a function
isotope_abundance which returns a table with the natural abundance of the
isotopes given an element symbol.
The table of the masses includes 2931 nuclides and is taken from
http://ie.lbl.gov/txt/awm95.txt
(G. Audi and A.H. Wapstra, Nucl. Phys. A595, 409, 1995)
The table of natural abundances includes 288 nuclides and is taken from the
Commission on Atomic Weights and Isotopic Abundances report for the
International Union of Pure and Applied Chemistry in Isotopic Compositions of
the Elements 1989, Pure and Applied Chemistry, 1998, 70, 217.
http://www.iupac.org/publications/pac/1998/pdf/7001x0217.pdf
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
%doc %{_mandir}/man3/Chemistry::Isotope.3pm*
%dir %{perl_vendorlib}/Chemistry/
%{perl_vendorlib}/Chemistry/Isotope.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.11-1
- Initial package.

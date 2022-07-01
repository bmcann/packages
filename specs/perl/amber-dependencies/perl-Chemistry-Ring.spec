# $Id$
# Authority: cmr
# Upstream: Ivan Tubert-Brohman <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-Ring

Name:           perl-Chemistry-Ring
Version:        0.20
Release:        2%{?dist}
Summary:        Perl module named Chemistry-Ring
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Chemistry-Ring

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivan Tubert-Brohman <itub@cpan.org>

Source:         http://www.cpan.org/modules/by-module/Chemistry/Chemistry-Ring-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Chemistry::Mol) >= 0.24
Requires:       perl(Statistics::Regression) >= 0.15

%description
This module provides some basic methods for representing a ring as a
substructure of a molecule. A ring is a subclass of molecule, because it has
atoms and bonds. Besides that, it has some useful geometric methods for finding
the centroid and the ring plane, and methods for aromaticity detection. This
module does not detect the rings by itself; for that, look at
Chemistry::Ring::Find. This module is part of the PerlMol project;
http://www.perlmol.org/.

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
%doc %{_mandir}/man3/Chemistry::Ring.3pm*
%doc %{_mandir}/man3/Chemistry::Ring::Find.3pm*
%dir %{perl_vendorlib}/Chemistry/
%{perl_vendorlib}/Chemistry/Ring/Find.pm
%{perl_vendorlib}/Chemistry/Ring.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.20-2
- Rebuilt for CentOS 7

* Thu Jul 16 2009 Unknown - 0.20-1
- Initial package. (using DAR)

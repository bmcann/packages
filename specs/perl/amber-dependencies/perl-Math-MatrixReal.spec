# $Id: perl-Math-MatrixReal.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Jonathan Leto <jonathan$leto,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-MatrixReal

Name:           perl-Math-MatrixReal
Version:        2.13
Release:        1%{?dist}
Summary:        Manipulate NxN matrices of real numbers
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Math-MatrixReal

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Jonathan Leto <jonathan@leto.net>

Source:         http://www.cpan.org/modules/by-module/Math/Math-MatrixReal-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Build) >= 0.38
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Most)

%description
The Math::MatrixReal package implements the data type "matrix of real numbers"
(and consequently also "vector of real numbers") which can be used almost like
any other Perl type thanks to operator overloading.

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
find %{buildroot} -name *.swo -exec %{__rm} -f {} \;

### Clean up docs
find example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644, root, root, 0755)
%doc CHANGES README.mkd CREDITS META.yml META.json MYMETA.yml MYMETA.json TODO example/
%doc %{_mandir}/man3/Math::Kleene.3pm*
%doc %{_mandir}/man3/Math::MatrixReal.3pm*
%dir %{perl_vendorlib}/Math/
%{perl_vendorlib}/Math/Kleene.pod
%{perl_vendorlib}/Math/MatrixReal.pm
%{perl_vendorlib}/Math/funcs.pl

%changelog
* Tue Jun 02 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 2.13-1
- Rebuilt for CentOS 7

* Mon Mar 03 2008 Dag Wieers <dag@wieers.com> - 2.05-1
- Updated to release 2.05.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 2.04-1
- Updated to release 2.04.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 2.03-1
- Updated to release 2.03.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Updated to release 2.02.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.01-1
- Updated to release 2.01.

* Tue Apr 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.9-1
- Initial package.

# $Id: perl-Math-VectorReal.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Anthony Thyssen <anthony$cit,gu,edu,au>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-VectorReal

Name:           perl-Math-VectorReal
Version:        1.02
Release:        2%{?dist}
Summary:        Module to handle 3D Vector Mathematics
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Math-VectorReal

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Anthony Thyssen <Anthony.Thyssen@gmail.com>

Source:         http://www.cpan.org/modules/by-module/Math/Math-VectorReal-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
The Math::VectorReal package defines a 3D mathematical "vector" in a way
that is compatible with the previous CPAN module Math::MatrixReal. However,
it provides a more vector-orientated set of mathematical functions and
overload operators to the MatrixReal package. For example, the normal perl string
functions "x" and "." have been overloaded to allow vector cross and dot
product operations. Vector math formula thus looks like vector math formula
in perl programs using this package.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644, root, root, 0755)
%doc Changes README MYMETA.yml MYMETA.json
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Math/
%{perl_vendorlib}/Math/VectorReal.pm
%{perl_vendorlib}/Math/*.pl

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 1.02-2
- Rebuilt for CentOS 7

* Mon Dec 06 2004 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.

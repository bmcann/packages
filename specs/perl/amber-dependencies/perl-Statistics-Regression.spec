# $Id$
# Authority: cmr
# Upstream: Ivo Welch <ivo.welch@yale.edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Statistics-Regression

Name:           perl-Statistics-Regression
Version:        0.53
Release:        2%{?dist}
Summary:        Weighted linear regression package (line+plane fitting)
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Statistics-Regression

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         Ivo Welch <ivo.welch@yale.edu>

Source:         http://www.cpan.org/modules/by-module/Statistics/Statistics-Regression-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl >= 0:5.005
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl >= 0:5.005

%description
Weighted linear regression package (line+plane fitting).

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
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Statistics/
%{perl_vendorlib}/Statistics/Regression.pm

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 0.53-2
- Rebuilt for CentOS 7

* Thu Jul 16 2009 Unknown - 0.53-1
- Initial package. (using DAR)

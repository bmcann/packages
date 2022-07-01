# $Id: perl-Parse-Yapp.spec 7981 2009-11-03 03:05:34Z dag $
# Authority: dries
# Upstream: Ivan Tubert <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parse-Yapp

Name:           perl-Parse-Yapp
Version:        1.21
Release:        1%{?dist}
Summary:        Perl extension for generating and using LALR parsers.
License:        Artistic/GPL
Group:          Applications/CPAN
URL:            https://metacpan.org/dist/Parse-Yapp

Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>
Vendor:         William N. Braswell, Jr. <wbraswell_cpan@NOSPAM.nym.hush.com>

Source:         http://www.cpan.org/modules/by-module/Parse/Parse-Yapp-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Parse::Yapp (Yet Another Perl Parser compiler) is a collection of modules that
let you generate and use yacc like thread safe (reentrant) parsers with perl
object oriented interface. The script yapp is a front-end to the Parse::Yapp
module and let you easily create a Perl OO parser from an input grammar file.

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
%doc %{_mandir}/man1/yapp.1*
%doc %{_mandir}/man3/Parse::Yapp.3*
%dir %{perl_vendorlib}/Parse/
%{perl_vendorlib}/Parse/Yapp/
%{perl_vendorlib}/Parse/Yapp.pm
%attr(0755, root, root) %{_bindir}/yapp

%changelog
* Wed Jun 03 2020 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 1.21-1
- Initial package.

# what it's called on pypi
%global srcname Automat
# what it's imported as
%global libname automat
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
Automat is a library for concise, idiomatic Python expression of finite-state
automata (particularly deterministic finite-state transducers).}

%bcond_with  tests
%bcond_without  python2

Name:           python-%{pkgname}
Version:        0.7.0
Release:        3.1%{?dist}
Summary:        Self-service finite-state machines for the programmer on the go

License:        MIT
URL:            https://github.com/glyph/automat
Source0:        %pypi_source
# PEP 570 adds "positional only" arguments to Python, which changes the
# code object constructor. This adds support for Python 3.8.
# https://github.com/glyph/automat/pull/111
Patch0:         0001-Add-support-for-positional-only-arguments.patch

BuildArch:      noarch

%{?python_enable_dependency_generator}

%description %{common_description}


%if %{with python2}
%package -n     python2-%{pkgname}
Summary:        %{summary}
Provides:       python2-%{libname}
%{?python_provide:%python_provide python2-%{pkgname}}

BuildRequires:  python2-devel
#BuildRequires:  python2-m2r
BuildRequires:  python2-setuptools
#BuildRequires:  python2-setuptools-scm
%if %{with tests}
BuildRequires:  python2dist(pytest)
BuildRequires:  python2dist(attrs) >= 16.1
BuildRequires:  python2dist(graphviz) > 0.5.1
BuildRequires:  python2dist(six)
BuildRequires:  python2dist(twisted) >= 16.1.1
%endif

%description -n python2-%{pkgname} %{common_description}
%endif


%prep
%autosetup  -p1 -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{eggname}.egg-info


%build
%if %{with python2}
%py2_build
%endif


%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%if %{with python2}
%py2_install
rm -rf %{buildroot}%{_bindir}/*
%endif


%check
%if %{with tests}
%if %{with python2}
PYTHONPATH=%{buildroot}%{python2_sitelib} pytest-%{python2_version} --verbose automat/_test
%endif
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} --verbose automat/_test
%endif


%if %{with python2}
%files -n python2-%{pkgname}
%license LICENSE
%doc README.md
%{python2_sitelib}/%{libname}
%{python2_sitelib}/%{eggname}-%{version}-py%{python2_version}.egg-info
%endif

%changelog
* Mon Jul 22 2019 Stephen Smoogen <smooge@fedora00.int.smoogespace.com> - 0.7.0-3.1
- Bootstrap version

* Mon May 27 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.0-3
- Add patch supporting for positional only arguments for Python 3.8

* Sat Apr 06 2019 Carl George <carl@george.computer> - 0.7.0-2
- Add provides for lowercase name
- Run tests with pytest like upstream does

* Mon Mar 11 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.0-1
- Release 0.7.0 (#1687495)

* Fri Mar 08 2019 Jeroen van Meeuwen <vanmeeuwen+fedora@kolabsys.com> - 0.6.0-5
 - Add bcond_without tests

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.7

* Fri Apr 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.0-1
- Initial package.

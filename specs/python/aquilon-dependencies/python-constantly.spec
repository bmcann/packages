# Created by pyp2rpm-3.3.2
%global pypi_name constantly

%global common_description %{expand:
A library that provides symbolic constant support. It includes
collections and constants with text, numeric, and bit flag values. Originally
twisted.python.constants from the Twisted project.}

Name:           python-%{pypi_name}
Version:        15.1.0
Release:        4%{?dist}
Summary:        Symbolic constants in Python

License:        MIT
URL:            https://github.com/twisted/constantly
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%{?python_enable_dependency_generator}

%description
%{common_description}


%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
%{common_description}


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py2_build


%install
%py2_install


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info



%changelog
* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 15.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 15.1.0-2
- Rebuilt for Python 3.7

* Mon May 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 15.1.0-1
- Initial package.

%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 0
%endif

%global srcname SQLAlchemy

Name:           python-sqlalchemy
Version:        1.3.6
Release:        1%{?dist}
Summary:        Modular and flexible ORM library for python

License:        MIT
URL:            http://www.sqlalchemy.org/
Source0:        https://files.pythonhosted.org/packages/source/S/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python2-devel >= 2.7
BuildRequires:  python2-setuptools
BuildRequires:  python2-mock
BuildRequires:  python2-pytest

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%endif

%description
SQLAlchemy is an Object Relational Mappper (ORM) that provides a flexible,
high-level interface to SQL databases.  Database and domain concepts are
decoupled, allowing both sides maximum flexibility and power. SQLAlchemy
provides a powerful mapping layer that can work as automatically or as manually
as you choose, determining relationships based on foreign keys or letting you
define the join conditions explicitly, to bridge the gap between database and
domain.

This package includes the python 2 version of the module.

%package doc
Summary:        Documentation for SQLAlchemy
BuildArch:      noarch

%description doc
Documentation for SQLAlchemy

%package -n python2-sqlalchemy
Summary:        Modular and flexible ORM library for python
%{?python_provide:%python_provide python2-sqlalchemy}

%description -n python2-sqlalchemy
SQLAlchemy is an Object Relational Mappper (ORM) that provides a flexible,
high-level interface to SQL databases.  Database and domain concepts are
decoupled, allowing both sides maximum flexibility and power. SQLAlchemy
provides a powerful mapping layer that can work as automatically or as manually
as you choose, determining relationships based on foreign keys or letting you
define the join conditions explicitly, to bridge the gap between database and
domain.

This package includes the python 2 version of the module.

%if 0%{?with_python3}
%package -n python3-sqlalchemy
Summary:        Modular and flexible ORM library for python
%{?python_provide:%python_provide python%{python3_pkgversion}-sqlalchemy}

%description -n python3-sqlalchemy
SQLAlchemy is an Object Relational Mappper (ORM) that provides a flexible,
high-level interface to SQL databases.  Database and domain concepts are
decoupled, allowing both sides maximum flexibility and power. SQLAlchemy
provides a powerful mapping layer that can work as automatically or as manually
as you choose, determining relationships based on foreign keys or letting you
define the join conditions explicitly, to bridge the gap between database and
domain.

This package includes the python 3 version of the module.
%endif # with_python3


%prep
%setup -n %{srcname}-%{version}

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif

# remove unnecessary scripts for building documentation
rm -rf doc/build

#%check
#PYTHONPATH=. %{__python2} -m pytest test
#
#%if 0%{?with_python3}
#PYTHONPATH=. %{__python3} -m pytest test
#%endif


%files doc
%doc doc examples

%files -n python2-sqlalchemy
%license LICENSE
%doc README.rst
%{python2_sitearch}/*

%if 0%{?with_python3}
%files -n python3-sqlalchemy
%license LICENSE
%doc README.rst
%{python3_sitearch}/*
%endif # with_python3

%changelog
* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Nils Philippsen <nils@tiptoe.de> - 1.2.17-1
- version 1.2.17

* Sat Jan 12 2019 Nils Philippsen <nils@tiptoe.de> - 1.2.16-1
- version 1.2.16

* Tue Oct 30 2018 Nils Philippsen <nils@tiptoe.de> - 1.2.12-1
- version 1.2.12

* Tue Aug 21 2018 Nils Philippsen <nils@tiptoe.de> - 1.2.11-1
- version 1.2.11

* Sun Jul 22 2018 Nils Philippsen <nils@tiptoe.de> - 1.2.10-1
- version 1.2.10

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Nils Philippsen <nils@tiptoe.de> - 1.2.8-3
- rename patch, apply with backups
- fix failing test for sqlite 3.24 instead of skipping it

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.8-2
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Nils Philippsen <nils@tiptoe.de> - 1.2.8-1
- version 1.2.8

* Sun Apr 22 2018 Nils Philippsen <nils@tiptoe.de> - 1.2.7-1
- version 1.2.7

* Sat Mar 31 2018 Nils Philippsen <nils@tiptoe.de> - 1.2.6-1
- version 1.2.6

* Mon Mar 19 2018 Nils Philippsen <nils@tiptoe.de> - 1.2.5-1
- version 1.2.5

* Tue Feb 27 2018 Nils Philippsen <nils@tiptoe.de> - 1.2.4-1
- version 1.2.4

* Tue Feb 20 2018 Nils Philippsen <nils@tiptoe.de> - 1.2.3-2
- require gcc for building

* Tue Feb 20 2018 Nils Philippsen <nils@tiptoe.de> - 1.2.3-1
- version 1.2.3

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Nils Philippsen <nils@tiptoe.de> - 1.2.2-1
- version 1.2.2

* Sun Dec 31 2017 Nils Philippsen <nils@tiptoe.de> - 1.2.0-1
- version 1.2.0
- fix version-releases in changelog

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 1.1.13-2
- Cleanup spec file conditionals

* Sat Aug 05 2017 Nils Philippsen <nils@tiptoe.de> - 1.1.13-1
- version 1.1.13

* Tue Aug 01 2017 Nils Philippsen <nils@tiptoe.de> - 1.1.12-1
- version 1.1.12
- remove comments with macros

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Nils Philippsen <nils@tiptoe.de> - 1.1.11-1
- version 1.1.11

* Sat May 27 2017 Nils Philippsen <nils@tiptoe.de> - 1.1.10-1
- version 1.1.10

* Thu Apr  6 2017 hguemar <hguemar@fedoraproject.org> - 1.1.9-1
- Upstream 1.1.9 (RHBZ#1436464)

* Wed Mar 15 2017 Nils Philippsen <nils@tiptoe.de> - 1.1.6-1
- version 1.1.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Nils Philippsen <nils@redhat.com> - 1.1.5-1
- version 1.1.5

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.1.4-3
- Enable tests

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.1.4-2
- Rebuild for Python 3.6
- Disable python3 tests for now

* Wed Nov 23 2016 Kevin Fenzi <kevin@scrye.com> - 1.1.4-1
- Update to 1.1.4. Fixes bug #1395470

* Tue Nov 8 2016 Orion Poplawski <orion@cora.nwra.com> - 1.1.3-2
- Ship python2-sqlalchemy
- Move docs into sub-package
- Modernize spec

* Mon Oct 31 2016 Kevin Fenzi <kevin@scrye.com> - 1.1.3-1
- Update to 1.1.3. Fixes bug #1389638

* Tue Oct 18 2016 Kevin Fenzi <kevin@scrye.com> - 1.1.2-1
- Update to 1.1.2. Fixes bug #1385990

* Mon Oct 10 2016 Nils Philippsen <nils@redhat.com> - 1.1.1-1
- version 1.1.1

* Thu Oct 06 2016 Kevin Fenzi <kevin@scrye.com> - 1.1.0-1
- Update to 1.1.0. Fixes bug #1382203

* Thu Aug 18 2016 Nils Philippsen <nils@redhat.com> - 1.0.14-1
- version 1.0.14

* Tue May 31 2016 Nils Philippsen <nils@redhat.com> - 1.0.14-1
- fix source URL

* Tue May 17 2016 Nils Philippsen <nils@redhat.com> - 1.0.13-1
- version 1.0.13

* Thu Feb 25 2016 Nils Philippsen <nils@redhat.com> - 1.0.12-1
- version 1.0.12

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Kevin Fenzi <kevin@scrye.com> - 1.0.11-1
- Update to 1.0.11. Fixes bug #1296757

* Sat Dec 12 2015 Kevin Fenzi <kevin@scrye.com> - 1.0.10-1
- Update to 1.0.10. Fixes bug #1290945

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 21 2015 Nils Philippsen <nils@redhat.com> - 1.0.9-1
- version 1.0.9, upstream feature and bugfix release

* Mon Oct 12 2015 Robert Kuska <rkuska@redhat.com> - 1.0.8-2
- Rebuilt for Python3.5 rebuild

* Fri Jul 24 2015 Nils Philippsen <nils@redhat.com> 1.0.8-1
- version 1.0.8, upstream bugfix release

* Tue Jul 21 2015 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7 (#1244991)

* Mon Jun 29 2015 Nils Philippsen <nils@redhat.com> 1.0.6-1
- version 1.0.6, upstream feature and bugfix release

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 07 2015 Kevin Fenzi <kevin@scrye.com> 1.0.4-1
- Update to 1.0.5. Fixes bug #1229067

* Fri May 08 2015 Nils Philippsen <nils@redhat.com> 1.0.4-1
- version 1.0.4, upstream bugfix release

* Sat May 02 2015 Kevin Fenzi <kevin@scrye.com> 1.0.3-1
- Update to 1.0.3. Fixes bug #1217761

* Sat Apr 25 2015 Nils Philippsen <nils@redhat.com> - 1.0.2-1
- version 1.0.2, upstream bugfix release

* Fri Apr 24 2015 Nils Philippsen <nils@redhat.com> - 1.0.1-1
- version 1.0.1, upstream bugfix release

* Fri Apr 17 2015 Nils Philippsen <nils@redhat.com> - 1.0.0-1
- version 1.0.0, upstream feature release

* Fri Apr 10 2015 Nils Philippsen <nils@redhat.com> - 0.9.9-1
- version 0.9.9, upstream feature and bugfix release

* Wed Oct 15 2014 Nils Philippsen <nils@redhat.com> - 0.9.8-1
- version 0.9.8, upstream feature and bugfix release
- avoid using unversioned python macros
- use py.test instead of nose for tests

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 29 2014 Nils Philippsen <nils@redhat.com> - 0.9.7-1
- version 0.9.7, upstream feature and bugfix release

* Mon Jun 30 2014 Nils Philippsen <nils@redhat.com> - 0.9.6-1
- version 0.9.6, upstream feature and bugfix release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu May 15 2014 Nils Philippsen <nils@redhat.com> - 0.9.4-1
- version 0.9.4, upstream feature and bugfix release

* Thu Feb 20 2014 Nils Philippsen <nils@redhat.com> - 0.9.3-1
- version 0.9.3, upstream feature and bugfix release

* Wed Feb 05 2014 Nils Philippsen <nils@redhat.com> - 0.9.2-1
- version 0.9.2, upstream feature and bugfix release

* Tue Jan 07 2014 Nils Philippsen <nils@redhat.com> - 0.9.1-1
- version 0.9.1, upstream feature and bugfix release
- no need to use 2to3 for python 3.x anymore
- build C extension for python 3.x
- require python2-devel >= 2.6 for building

* Mon Dec 09 2013 Nils Philippsen <nils@redhat.com> - 0.8.4-1
- version 0.8.4, upstream bugfix release

* Tue Oct 29 2013 Nils Philippsen <nils@redhat.com> - 0.8.3-1
- version 0.8.3, upstream bugfix release

* Wed Aug 14 2013 Nils Philippsen <nils@redhat.com> - 0.8.2-1
- version 0.8.2, upstream bugfix release
- drop obsolete sqlalchemy-test-bidirectional-order patch
- fix bogus date in changelog

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8.1-1
- Upstream bugfix
- Stop calling sa2to3 explicitly on the library.  It seems to break mapper.py's
  import of collections.deque

* Fri Apr 12 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8.0-1
- Final release of 0.8.0
- Fix for a unittest that assumes order in dicts

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-0.2.b1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov  1 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8.0-0.1.b1
- Update to 0.8.0 beta

* Mon Aug 13 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7.8-4.20120813hg8535
- Update to a snapshot to fix unittest errors with python-3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 0.7.8-3
- remove rhel logic from with_python3 conditional

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 18 2012 Nils Philippsen <nils@redhat.com> - 0.7.8-1
- Upstream bugfix release

* Tue May 15 2012 Nils Philippsen <nils@redhat.com> - 0.7.7-1
- Upstream bugfix release

* Tue Mar 20 2012 Nils Philippsen <nils@redhat.com> - 0.7.6-1
- Upstream bugfix release

* Mon Jan 30 2012 Nils Philippsen <nils@redhat.com> - 0.7.5-1
- Upstream bugfix release
- package README.rst instead of README as documentation

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 0.7.3-2
- rebuild for gcc 4.7

* Mon Oct 17 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7.3-1
- Upstream bugfix release

* Mon Aug 1 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7.2-1
- Upstream bugfix release

* Mon Jun 06 2011 Nils Philippsen <nils@redhat.com> - 0.7.1-1
- 0.7.1 Upstream release
- no need to fix examples/dynamic_dict/dynamic_dict.py anymore
- use sqla_nose.py to fix %%check

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.6-1
- 0.6.6 Upstream release

* Fri Dec 3 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.5-1
- 0.6.5 Upstream release

* Wed Sep 29 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.4-2
- Filter out the C extensions from provides

* Tue Sep 07 2010 Luke Macken <lmacken@redhat.com> - 0.6.4-1
- 0.6.4 upstream release

* Mon Aug 23 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.3-1
- 0.6.3 upstream release

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com>
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 24 2010 Nils Philippsen <nils@redhat.com> - 0.6.1-1
- 0.6.1 upstream release

* Tue Apr 13 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6-0.4.beta3
- Build beta3

* Fri Mar 19 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6-0.3.beta2
- Build beta2 with cextension

* Sun Mar 7 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6-0.2.beta1
- Build python3 package

* Tue Mar 2 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6-0.1.beta1
- 0.6 beta1 upstream release

* Tue Feb 2 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.5.8-3
- One last cleanup

* Tue Feb 2 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.5.8-2
- just some cleanups to older styles of building packages.

* Mon Feb 1 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.5.8-1
- Upstream bugfix release 0.5.8

* Fri Aug 14 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.5.5-2
- Upstream bugfix release 0.5.5

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2.p2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 12 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.5.4-1.p2
- Upstream bugfix release 0.5.4p2.

* Thu Apr 16 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.5.3-1
- Upstream bugfix release.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Wed Jan 21 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1.

* Mon Dec 1 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.5-0.1.rc4
- Update to 0.5.0rc4 which works with the new pysqlite
- And update test cases to work with the new pysqlite

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.4.7-2
- Rebuild for Python 2.6

* Sun Jul 27 2008 Toshio Kuratomi <toshio@fedoraproject.org> 0.4.7-1
- Update to 0.4.7.

* Sun Jun 1 2008 Toshio Kuratomi <toshio@fedoraproject.org> 0.4.6-1
- Update to 0.4.6.

* Tue Apr 8 2008 Toshio Kuratomi <toshio@fedoraproject.org> 0.4.5-1
- Update to 0.4.5.

* Fri Feb 22 2008 Toshio Kuratomi <toshio@fedoraproject.org> 0.4.3-1
- Update to 0.4.3.

* Tue Dec 11 2007 Toshio Kuratomi <a.badger@gmail.com> 0.4.2-1.p3
- Update to 0.4.2p3.

* Tue Dec 11 2007 Toshio Kuratomi <a.badger@gmail.com> 0.4.1-1
- Update to 0.4.1.

* Wed Oct 17 2007 Toshio Kuratomi <a.badger@gmail.com> 0.4.0-1
- SQLAlchemy-0.4.0 final
- Run the testsuite

* Wed Oct  3 2007 Luke Macken <lmacken@redhat.com> 0.4.0-0.4.beta6
- SQLAlchemy-0.4.0beta6

* Tue Sep 11 2007 Toshio Kuratomi <a.badger@gmail.com> - 0.4.0-0.4.beta5
- Update to 0.4beta5.

* Fri Sep 07 2007 Toshio Kuratomi <a.badger@gmail.com> - 0.4.0-0.4.beta4
- setuptools has been fixed.

* Fri Aug 31 2007 Toshio Kuratomi <a.badger@gmail.com> - 0.4.0-0.3.beta4
- setuptools seems to be broken WRT having an active and inactive version
  of an egg.  Have to make both versions inactive and manually setup a copy
  that can be started via import. (Necessary for the sqlalchemy0.3 compat
  package.)

* Tue Aug 28 2007 Toshio Kuratomi <a.badger@gmail.com> - 0.4.0-0.2.beta4
- Modify setuptools to handle the -devel subpackage split in F-8.

* Mon Aug 27 2007 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.4.0-0.1.beta4
- Update to 0.4 beta4.

* Tue Jul 24 2007 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.3.10-2
- Remove python-abi Requires.  This is automatic since FC4+.

* Tue Jul 24 2007 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.3.10-1
- Update to new upstream version 0.3.10

* Fri Mar 23 2007 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.3.6-1
- Update to new upstream version 0.3.6

* Sat Mar 10 2007 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.3.5-1
- Update to new upstream version 0.3.5
- Simplify the files listing

* Tue Jan 23 2007 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.3.4-2
- Remember to upload the source tarball to the lookaside cache.

* Tue Jan 23 2007 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.3.4-1
- Update to new upstream version 0.3.4

* Mon Jan 01 2007 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.3.3-1
- Update to new upstream version 0.3.3

* Sat Dec 09 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.3.1-2
- Bump and rebuild for python 2.5 on devel.
- BuildRequire: python-devel as a header is missing otherwise.

* Fri Nov 24 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.3.1-1
- Update to new upstream version 0.3.1

* Sat Sep 16 2006 Shahms E. King <shahms@shahms.com> 0.2.7-2
- Rebuild for FC6

* Thu Aug 17 2006 Shahms E. King <shahms@shahms.com> 0.2.7-1
- Update to new upstream version

* Fri Aug 11 2006 Shahms E. King <shahms@shahms.com> 0.2.6-2
- Include, don't ghost .pyo files per new guidelines

* Tue Aug 08 2006 Shahms E. King <shahms@shahms.com> 0.2.6-1
- Update to new upstream version

* Fri Jul 07 2006 Shahms E. King <shahms@shahms.com> 0.2.4-1
- Update to new upstream version

* Mon Jun 26 2006 Shahms E. King <shahms@shahms.com> 0.2.3-1
- Update to new upstream version

* Wed May 31 2006 Shahms E. King <shahms@shahms.com> 0.2.1-1
- Update to new upstream version

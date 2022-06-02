Name:           ncm-spma
Version:        21.12.1
Release:        1
Summary:        NCM component for spma

License:        ASL 2.0 and EU Datagrid
Group:          System Environment/Base
URL:            https://github.com/quattor/configuration-modules-core/tree/master/ncm-spma
Source0:        %{name}-%{version}.tar.gz
Source1:        spmaleaves.py

Vendor:         Quattor
Packager:       Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie>

BuildArch:      noarch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: perl(CAF::FileEditor)
Requires: perl(CAF::FileWriter)
Requires: perl(CAF::Object)
Requires: perl(CAF::Path)
Requires: perl(CAF::Process)
Requires: perl(EDG::WP4::CCM::Path)
Requires: perl(EDG::WP4::CCM::Path) >= 16.8.0
Requires: perl(EDG::WP4::CCM::TextRender)
Requires: perl(File::Basename)
Requires: perl(File::Copy)
Requires: perl(File::Path)
Requires: perl(File::Temp)
Requires: perl(LC::Exception)
Requires: perl(NCM::Component)
Requires: perl(NCM::Component::spma::yum)
Requires: perl(POSIX)
Requires: perl(Set::Scalar)
Requires: perl(Text::Glob)
Requires: perl(constant)
Requires: perl(parent)
Requires: perl(strict)
Requires: perl(warnings)
Requires: rpmlib(CompressedFileNames) <= 3.0.4-1
Requires: rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires: yum >= 3.2.29
Requires: yum-priorities
Requires: yum-utils >= 1.1.30
Requires: yum-versionlock

Provides: perl(NCM::Component::spma)
Provides: perl(NCM::Component::spma::dnf)
Provides: perl(NCM::Component::spma::yum)
Provides: perl(NCM::Component::spma::yumdnf)
Provides: perl(NCM::Component::spma::yumng)

%description
%{name}

%prep
cd ~/rpmbuild/BUILD
%{__rm} -rf usr spmaleaves.py
/usr/bin/gzip -dc ~/rpmbuild/SOURCES/%{name}-%{version}.tar.gz | /usr/bin/tar -xof -
STATUS=$?
if [ $STATUS -ne 0 ]; then
    exit $STATUS
fi
%{__cp} -a %{_topdir}/SOURCES/spmaleaves.py ./

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/%{_prefix}/lib/perl/NCM/Component
%{__mkdir} -p %{buildroot}/%{_prefix}/lib/perl/NCM/Component/spma
%{__mkdir} -p %{buildroot}/%{_sbindir}
%{__mkdir} -p %{buildroot}/%{_docdir}
%{__mkdir} -p %{buildroot}/%{_docdir}/ncm-spma-21.12.0
%{__mkdir} -p %{buildroot}/%{_docdir}/pan/components/spma
%{__mkdir} -p %{buildroot}/%{_docdir}/pan/components/spma/apt
%{__mkdir} -p %{buildroot}/%{_docdir}/pan/components/spma/dnf
%{__mkdir} -p %{buildroot}/%{_docdir}/pan/components/spma/ips
%{__mkdir} -p %{buildroot}/%{_docdir}/pan/components/spma/yum
%{__mkdir} -p %{buildroot}/%{_docdir}/pan/components/spma/yumdnf
%{__mkdir} -p %{buildroot}/%{_docdir}/pan/components/spma/yumng
%{__mkdir} -p %{buildroot}/%{_mandir}/man8
%{__mkdir} -p %{buildroot}/%{_datadir}/templates/quattor/spma
%{__mkdir} -p %{buildroot}/%{_datadir}/templates/quattor/spma/apt
%{__mkdir} -p %{buildroot}/%{_datadir}/templates/quattor/spma/yumplugins
%{__mkdir} -p %{buildroot}/%{_datadir}/quattor/spma/yumdnf
%{__install} -m 644 usr/lib/perl/NCM/Component/spma.pm %{buildroot}/%{_prefix}/lib/perl/NCM/Component/
%{__install} -m 644 usr/lib/perl/NCM/Component/spma/dnf.pm %{buildroot}/%{_prefix}/lib/perl/NCM/Component/spma/
%{__install} -m 644 usr/lib/perl/NCM/Component/spma/yum.pm %{buildroot}/%{_prefix}/lib/perl/NCM/Component/spma/
%{__install} -m 644 usr/lib/perl/NCM/Component/spma/yumdnf.pm %{buildroot}/%{_prefix}/lib/perl/NCM/Component/spma/
%{__install} -m 644 usr/lib/perl/NCM/Component/spma/yumng.pm %{buildroot}/%{_prefix}/lib/perl/NCM/Component/spma/
%{__install} -m 750 usr/sbin/spma %{buildroot}/%{_sbindir}/
%{__install} -m 644 usr/share/doc/ncm-spma-21.12.0/ChangeLog.template %{buildroot}/%{_docdir}/ncm-spma-21.12.0/
%{__install} -m 644 usr/share/doc/pan/components/spma/apt/config.pan %{buildroot}/%{_docdir}/pan/components/spma/apt/
%{__install} -m 644 usr/share/doc/pan/components/spma/apt/schema.pan %{buildroot}/%{_docdir}/pan/components/spma/apt/
%{__install} -m 644 usr/share/doc/pan/components/spma/config-common-yum.pan %{buildroot}/%{_docdir}/pan/components/spma/
%{__install} -m 644 usr/share/doc/pan/components/spma/config-common.pan %{buildroot}/%{_docdir}/pan/components/spma/
%{__install} -m 644 usr/share/doc/pan/components/spma/config.pan %{buildroot}/%{_docdir}/pan/components/spma/
%{__install} -m 644 usr/share/doc/pan/components/spma/dnf/config.pan %{buildroot}/%{_docdir}/pan/components/spma/dnf/
%{__install} -m 644 usr/share/doc/pan/components/spma/dnf/schema.pan %{buildroot}/%{_docdir}/pan/components/spma/dnf/
%{__install} -m 644 usr/share/doc/pan/components/spma/functions.pan %{buildroot}/%{_docdir}/pan/components/spma/
%{__install} -m 644 usr/share/doc/pan/components/spma/ips/config.pan %{buildroot}/%{_docdir}/pan/components/spma/ips/
%{__install} -m 644 usr/share/doc/pan/components/spma/ips/schema.pan %{buildroot}/%{_docdir}/pan/components/spma/ips/
%{__install} -m 644 usr/share/doc/pan/components/spma/light.pan %{buildroot}/%{_docdir}/pan/components/spma/
%{__install} -m 644 usr/share/doc/pan/components/spma/repository_cleanup.pan %{buildroot}/%{_docdir}/pan/components/spma/
%{__install} -m 644 usr/share/doc/pan/components/spma/schema-common-yum.pan %{buildroot}/%{_docdir}/pan/components/spma/
%{__install} -m 644 usr/share/doc/pan/components/spma/schema.pan %{buildroot}/%{_docdir}/pan/components/spma/
%{__install} -m 644 usr/share/doc/pan/components/spma/software.pan %{buildroot}/%{_docdir}/pan/components/spma/
%{__install} -m 644 usr/share/doc/pan/components/spma/yum/config.pan %{buildroot}/%{_docdir}/pan/components/spma/yum/
%{__install} -m 644 usr/share/doc/pan/components/spma/yum/light.pan %{buildroot}/%{_docdir}/pan/components/spma/yum/
%{__install} -m 644 usr/share/doc/pan/components/spma/yum/schema.pan %{buildroot}/%{_docdir}/pan/components/spma/yum/
%{__install} -m 644 usr/share/doc/pan/components/spma/yumdnf/config.pan %{buildroot}/%{_docdir}/pan/components/spma/yumdnf/
%{__install} -m 644 usr/share/doc/pan/components/spma/yumdnf/light.pan %{buildroot}/%{_docdir}/pan/components/spma/yumdnf/
%{__install} -m 644 usr/share/doc/pan/components/spma/yumdnf/schema.pan %{buildroot}/%{_docdir}/pan/components/spma/yumdnf/
%{__install} -m 644 usr/share/doc/pan/components/spma/yumng/config.pan %{buildroot}/%{_docdir}/pan/components/spma/yumng/
%{__install} -m 644 usr/share/doc/pan/components/spma/yumng/schema.pan %{buildroot}/%{_docdir}/pan/components/spma/yumng/
%{__install} -m 644 usr/share/man/man8/NCM::Component::spma.8.gz %{buildroot}/%{_mandir}/man8/
%{__install} -m 644 usr/share/man/man8/NCM::Component::spma::dnf.8.gz %{buildroot}/%{_mandir}/man8/
%{__install} -m 644 usr/share/man/man8/NCM::Component::spma::yum.8.gz %{buildroot}/%{_mandir}/man8/
%{__install} -m 644 usr/share/man/man8/NCM::Component::spma::yumdnf.8.gz %{buildroot}/%{_mandir}/man8/
%{__install} -m 644 usr/share/man/man8/NCM::Component::spma::yumng.8.gz %{buildroot}/%{_mandir}/man8/
%{__install} -m 644 usr/share/templates/quattor/spma/apt/config.tt %{buildroot}/%{_datadir}/templates/quattor/spma/apt/
%{__install} -m 644 usr/share/templates/quattor/spma/apt/preferences.tt %{buildroot}/%{_datadir}/templates/quattor/spma/apt/
%{__install} -m 644 usr/share/templates/quattor/spma/apt/source.tt %{buildroot}/%{_datadir}/templates/quattor/spma/apt/
%{__install} -m 644 usr/share/templates/quattor/spma/dnf_module.tt %{buildroot}/%{_datadir}/templates/quattor/spma/
%{__install} -m 644 usr/share/templates/quattor/spma/repository.tt %{buildroot}/%{_datadir}/templates/quattor/spma/
%{__install} -m 644 usr/share/templates/quattor/spma/yumplugins/fastestmirror.tt %{buildroot}/%{_datadir}/templates/quattor/spma/yumplugins/
%{__install} -m 644 usr/share/templates/quattor/spma/yumplugins/generic.tt %{buildroot}/%{_datadir}/templates/quattor/spma/yumplugins/
%{__install} -m 644 usr/share/templates/quattor/spma/yumplugins/priorities.tt %{buildroot}/%{_datadir}/templates/quattor/spma/yumplugins/
%{__install} -m 644 usr/share/templates/quattor/spma/yumplugins/product-id.tt %{buildroot}/%{_datadir}/templates/quattor/spma/yumplugins/
%{__install} -m 644 usr/share/templates/quattor/spma/yumplugins/subscription-manager.tt %{buildroot}/%{_datadir}/templates/quattor/spma/yumplugins/
%{__install} -m 644 usr/share/templates/quattor/spma/yumplugins/versionlock.tt %{buildroot}/%{_datadir}/templates/quattor/spma/yumplugins/
%{__install} -m 644 spmaleaves.py %{buildroot}/%{_datadir}/quattor/spma/yumdnf/

%post
if [ -x /usr/bin/dnf ]; then
    # from dnf.const.PLUGINPATH
    pylib=$(/usr/libexec/platform-python -c 'import distutils.sysconfig;print(distutils.sysconfig.get_python_lib())')
    plugin="$pylib/dnf-plugins/spmaleaves.py"
    if [ ! -f $plugin ]; then
        ln -s /usr/share/quattor/spma/yumdnf/spmaleaves.py $plugin
    fi
fi

%preun
if [ $1 == 0 ]; then
    if [ -x /usr/bin/dnf ]; then
        # from dnf.const.PLUGINPATH
        pylib=$(/usr/libexec/platform-python -c 'import distutils.sysconfig;print(distutils.sysconfig.get_python_lib())')
        plugin="$pylib/dnf-plugins/spmaleaves.py"
        if [ -f $plugin ]; then
            rm -f $plugin
            rm -f "$pylib"/dnf-plugins/__pycache__/spmaleaves.*.pyc
        fi
    fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}/lib/perl/NCM/Component/spma.pm
%{_prefix}/lib/perl/NCM/Component/spma/dnf.pm
%{_prefix}/lib/perl/NCM/Component/spma/yum.pm
%{_prefix}/lib/perl/NCM/Component/spma/yumdnf.pm
%{_prefix}/lib/perl/NCM/Component/spma/yumng.pm
%{_sbindir}/spma
%{_docdir}/ncm-spma-21.12.0/ChangeLog.template
%{_docdir}/pan/components/spma/apt/config.pan
%{_docdir}/pan/components/spma/apt/schema.pan
%{_docdir}/pan/components/spma/config-common-yum.pan
%{_docdir}/pan/components/spma/config-common.pan
%{_docdir}/pan/components/spma/config.pan
%{_docdir}/pan/components/spma/dnf/config.pan
%{_docdir}/pan/components/spma/dnf/schema.pan
%{_docdir}/pan/components/spma/functions.pan
%{_docdir}/pan/components/spma/ips/config.pan
%{_docdir}/pan/components/spma/ips/schema.pan
%{_docdir}/pan/components/spma/light.pan
%{_docdir}/pan/components/spma/repository_cleanup.pan
%{_docdir}/pan/components/spma/schema-common-yum.pan
%{_docdir}/pan/components/spma/schema.pan
%{_docdir}/pan/components/spma/software.pan
%{_docdir}/pan/components/spma/yum/config.pan
%{_docdir}/pan/components/spma/yum/light.pan
%{_docdir}/pan/components/spma/yum/schema.pan
%{_docdir}/pan/components/spma/yumdnf/config.pan
%{_docdir}/pan/components/spma/yumdnf/light.pan
%{_docdir}/pan/components/spma/yumdnf/schema.pan
%{_docdir}/pan/components/spma/yumng/config.pan
%{_docdir}/pan/components/spma/yumng/schema.pan
%{_mandir}/man8/NCM::Component::spma.8.gz
%{_mandir}/man8/NCM::Component::spma::dnf.8.gz
%{_mandir}/man8/NCM::Component::spma::yum.8.gz
%{_mandir}/man8/NCM::Component::spma::yumdnf.8.gz
%{_mandir}/man8/NCM::Component::spma::yumng.8.gz
%{_datadir}/templates/quattor/spma/apt/config.tt
%{_datadir}/templates/quattor/spma/apt/preferences.tt
%{_datadir}/templates/quattor/spma/apt/source.tt
%{_datadir}/templates/quattor/spma/dnf_module.tt
%{_datadir}/templates/quattor/spma/repository.tt
%{_datadir}/templates/quattor/spma/yumplugins/fastestmirror.tt
%{_datadir}/templates/quattor/spma/yumplugins/generic.tt
%{_datadir}/templates/quattor/spma/yumplugins/priorities.tt
%{_datadir}/templates/quattor/spma/yumplugins/product-id.tt
%{_datadir}/templates/quattor/spma/yumplugins/subscription-manager.tt
%{_datadir}/templates/quattor/spma/yumplugins/versionlock.tt
%{_datadir}/quattor/spma/yumdnf/spmaleaves.py
%exclude %{_datadir}/quattor/spma/yumdnf/spmaleaves.pyc
%exclude %{_datadir}/quattor/spma/yumdnf/spmaleaves.pyo

%changelog
* Mon Feb 14 2022 Tacaíocht Ríomhaireachta <tacaiocht.riomhaireachta@ucd.ie> - 21.12.1-1
- Repackage ncm-spma with patches to enable dnf usage on EL8 from upstream

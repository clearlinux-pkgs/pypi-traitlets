#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : traitlets
Version  : 5.0.5
Release  : 39
URL      : https://files.pythonhosted.org/packages/b8/24/e6dfe45ecfc4c2b0d6774565e631dc1b9e50de2c3536625d377963d56cae/traitlets-5.0.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/b8/24/e6dfe45ecfc4c2b0d6774565e631dc1b9e50de2c3536625d377963d56cae/traitlets-5.0.5.tar.gz
Summary  : Traitlets Python configuration system
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: traitlets-license = %{version}-%{release}
Requires: traitlets-python = %{version}-%{release}
Requires: traitlets-python3 = %{version}-%{release}
Requires: decorator
Requires: ipython_genutils
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : decorator
BuildRequires : six

%description
# Traitlets
[![Build Status](https://travis-ci.org/ipython/traitlets.svg?branch=master)](https://travis-ci.org/ipython/traitlets)
[![Documentation Status](https://readthedocs.org/projects/traitlets/badge/?version=latest)](https://traitlets.readthedocs.io/en/latest/?badge=latest)

%package license
Summary: license components for the traitlets package.
Group: Default

%description license
license components for the traitlets package.


%package python
Summary: python components for the traitlets package.
Group: Default
Requires: traitlets-python3 = %{version}-%{release}

%description python
python components for the traitlets package.


%package python3
Summary: python3 components for the traitlets package.
Group: Default
Requires: python3-core
Provides: pypi(traitlets)
Requires: pypi(ipython_genutils)

%description python3
python3 components for the traitlets package.


%prep
%setup -q -n traitlets-5.0.5
cd %{_builddir}/traitlets-5.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602778815
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/traitlets
cp %{_builddir}/traitlets-5.0.5/COPYING.md %{buildroot}/usr/share/package-licenses/traitlets/42f5ceb01d59f395d5376b6a6e2af3a99ea0873f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/traitlets/42f5ceb01d59f395d5376b6a6e2af3a99ea0873f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

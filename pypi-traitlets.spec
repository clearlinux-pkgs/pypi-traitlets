#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-traitlets
Version  : 5.2.0
Release  : 58
URL      : https://files.pythonhosted.org/packages/74/12/24da62eebb4272e342a011cc04e88f7ed0bbe613ed863f9718402387d063/traitlets-5.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/74/12/24da62eebb4272e342a011cc04e88f7ed0bbe613ed863f9718402387d063/traitlets-5.2.0.tar.gz
Summary  : Traitlets Python configuration system
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-traitlets-license = %{version}-%{release}
Requires: pypi-traitlets-python = %{version}-%{release}
Requires: pypi-traitlets-python3 = %{version}-%{release}
Requires: pypi(decorator)
Requires: pypi(ipython_genutils)
Requires: pypi(six)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)

%description
# Traitlets
[![Tests](https://github.com/ipython/traitlets/actions/workflows/tests.yml/badge.svg)](https://github.com/ipython/traitlets/actions/workflows/tests.yml)
[![Test downstream projects](https://github.com/ipython/traitlets/actions/workflows/downstream.yml/badge.svg)](https://github.com/ipython/traitlets/actions/workflows/downstream.yml)
[![Documentation Status](https://readthedocs.org/projects/traitlets/badge/?version=latest)](https://traitlets.readthedocs.io/en/latest/?badge=latest)

%package license
Summary: license components for the pypi-traitlets package.
Group: Default

%description license
license components for the pypi-traitlets package.


%package python
Summary: python components for the pypi-traitlets package.
Group: Default
Requires: pypi-traitlets-python3 = %{version}-%{release}

%description python
python components for the pypi-traitlets package.


%package python3
Summary: python3 components for the pypi-traitlets package.
Group: Default
Requires: python3-core
Provides: pypi(traitlets)

%description python3
python3 components for the pypi-traitlets package.


%prep
%setup -q -n traitlets-5.2.0
cd %{_builddir}/traitlets-5.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652194078
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-traitlets
cp %{_builddir}/traitlets-5.2.0/COPYING.md %{buildroot}/usr/share/package-licenses/pypi-traitlets/2c15eff35efcbd62ef860412b46613a6a194fbc3
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-traitlets/2c15eff35efcbd62ef860412b46613a6a194fbc3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

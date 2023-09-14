#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-traitlets
Version  : 5.10.0
Release  : 76
URL      : https://files.pythonhosted.org/packages/1a/19/381eb24d3bf6d3038bfd63263e2456fd1334d5a93d5f3953de6f06b276b5/traitlets-5.10.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/1a/19/381eb24d3bf6d3038bfd63263e2456fd1334d5a93d5f3953de6f06b276b5/traitlets-5.10.0.tar.gz
Summary  : Traitlets Python configuration system
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-traitlets-python = %{version}-%{release}
Requires: pypi-traitlets-python3 = %{version}-%{release}
Requires: pypi(decorator)
Requires: pypi(ipython_genutils)
Requires: pypi(six)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Traitlets
[![Tests](https://github.com/ipython/traitlets/actions/workflows/tests.yml/badge.svg)](https://github.com/ipython/traitlets/actions/workflows/tests.yml)
[![Documentation Status](https://readthedocs.org/projects/traitlets/badge/?version=latest)](https://traitlets.readthedocs.io/en/latest/?badge=latest)
[![Tidelift](https://tidelift.com/subscription/pkg/pypi-traitlets)](https://tidelift.com/badges/package/pypi/traitlets)

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
%setup -q -n traitlets-5.10.0
cd %{_builddir}/traitlets-5.10.0
pushd ..
cp -a traitlets-5.10.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694707643
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

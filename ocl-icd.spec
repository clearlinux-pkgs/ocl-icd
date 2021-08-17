#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ocl-icd
Version  : 2.3.1
Release  : 17
URL      : https://github.com/OCL-dev/ocl-icd/archive/v2.3.1/ocl-icd-2.3.1.tar.gz
Source0  : https://github.com/OCL-dev/ocl-icd/archive/v2.3.1/ocl-icd-2.3.1.tar.gz
Summary  : Open Computing Language generic Installable Client Driver support
Group    : Development/Tools
License  : BSD-2-Clause
Requires: ocl-icd-lib = %{version}-%{release}
Requires: ocl-icd-license = %{version}-%{release}
BuildRequires : ruby

%description
This package aims at creating an Open Source alternative to vendor specific
OpenCL ICD loaders.

%package dev
Summary: dev components for the ocl-icd package.
Group: Development
Requires: ocl-icd-lib = %{version}-%{release}
Provides: ocl-icd-devel = %{version}-%{release}
Requires: ocl-icd = %{version}-%{release}

%description dev
dev components for the ocl-icd package.


%package doc
Summary: doc components for the ocl-icd package.
Group: Documentation

%description doc
doc components for the ocl-icd package.


%package lib
Summary: lib components for the ocl-icd package.
Group: Libraries
Requires: ocl-icd-license = %{version}-%{release}

%description lib
lib components for the ocl-icd package.


%package license
Summary: license components for the ocl-icd package.
Group: Default

%description license
license components for the ocl-icd package.


%prep
%setup -q -n ocl-icd-2.3.1
cd %{_builddir}/ocl-icd-2.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629234376
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
%reconfigure --disable-static --enable-custom-vendordir=/usr/share/OpenCL/vendors
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1629234376
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ocl-icd
cp %{_builddir}/ocl-icd-2.3.1/COPYING %{buildroot}/usr/share/package-licenses/ocl-icd/6e27f34439f0059927381892f5dc3e19605a4776
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/ocl_icd.h
/usr/lib64/libOpenCL.so
/usr/lib64/pkgconfig/OpenCL.pc
/usr/lib64/pkgconfig/ocl-icd.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/ocl\-icd/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libOpenCL.so.1
/usr/lib64/libOpenCL.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ocl-icd/6e27f34439f0059927381892f5dc3e19605a4776

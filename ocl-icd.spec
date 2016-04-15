#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ocl-icd
Version  : 2.2.9
Release  : 1
URL      : https://github.com/OCL-dev/ocl-icd/archive/v2.2.9.tar.gz
Source0  : https://github.com/OCL-dev/ocl-icd/archive/v2.2.9.tar.gz
Summary  : Open Computing Language generic Installable Client Driver support
Group    : Development/Tools
License  : BSD-2-Clause
Requires: ocl-icd-lib
Requires: ocl-icd-doc
BuildRequires : ruby

%description
This package aims at creating an Open Source alternative to vendor specific
OpenCL ICD loaders.

%package dev
Summary: dev components for the ocl-icd package.
Group: Development
Requires: ocl-icd-lib
Provides: ocl-icd-devel

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

%description lib
lib components for the ocl-icd package.


%prep
cd ..
%setup -q -n ocl-icd-2.2.9

%build
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/ocl-icd/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

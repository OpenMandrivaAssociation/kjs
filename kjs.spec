%define major 5
%define libname %mklibname KF5JS %{major}
%define devname %mklibname KF5JS -d
%define debug_package %{nil}

Name: kjs
Version: 5.1.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/frameworks/%{version}/portingAids/%{name}-%{version}.tar.xz
Patch0: kjs-4.96.0-fix-create_hash_table-location.patch
Summary: The KDE Frameworks 5 JavaScript library
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: qmake5
BuildRequires: cmake
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(libpcre)
Requires: %{libname} = %{EVRD}

%description
The KDE Frameworks 5 JavaScript library.

%package -n %{libname}
Summary: The KDE Frameworks 5 JavaScript library
Group: System/Libraries

%description -n %{libname}
The KDE Frameworks 5 JavaScript library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{name} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
#apply_patches
%cmake

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5

%files
%{_bindir}/*
%{_datadir}/kf5/kjs

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*

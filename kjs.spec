%define major 5
%define libname %mklibname KF5JS %{major}
%define apilibname %mklibname KF5JSApi %{major}
%define devname %mklibname KF5JS -d
%define debug_package %{nil}

Name: kjs
Version: 4.95.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/4.95.0/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 JavaScript library
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: qmake5
BuildRequires: cmake
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(libpcre)
Requires: %{libname} = %{EVRD}
Requires: %{apilibname} = %{EVRD}

%description
The KDE Frameworks 5 JavaScript library.

%package -n %{libname}
Summary: The KDE Frameworks 5 JavaScript library
Group: System/Libraries

%description -n %{libname}
The KDE Frameworks 5 JavaScript library.

%package -n %{apilibname}
Summary: KDE Frameworks 5 JavaScript API library
Group: System/Libraries

%description -n %{apilibname}
KDE Frameworks 5 JavaScript API library

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_bindir}/*
%{_datadir}/kjs

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*

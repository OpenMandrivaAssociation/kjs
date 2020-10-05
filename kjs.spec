%define major 5
%define libname %mklibname KF5JS %{major}
%define devname %mklibname KF5JS -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%global optflags %{optflags} -O3

Name: kjs
Version: 5.75.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/portingAids/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 JavaScript library
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
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
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kjs5 --with-man

%files -f kjs5.lang
%{_bindir}/*
%{_datadir}/kf5/kjs
%{_mandir}/man1/kjs5.1.*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*

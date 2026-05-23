%bcond clang 1
%bcond gamin 1

# TDE variables
%define tde_pkg tdeio-locate
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	Tdeio-slave for the locate command [Trinity]
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/tdeio/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils

BuildRequires:	libtool

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes


# ACL support
BuildRequires:  pkgconfig(libacl)

# IDN support
BuildRequires:	pkgconfig(libidn)

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}


# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

Obsoletes:		trinity-kio-locate < %{EVRD}
Provides:		trinity-kio-locate = %{EVRD}


%description
Adds support for the "locate" and "locater:"
protocols to Konqueror and other TDE applications.

This enables you to perform locate searches as you
would in a terminal. The result is displayed just
as a directory.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"


%install -a
%find_lang tdeio_locate


%files -f tdeio_locate.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING TODO
%{tde_prefix}/%{_lib}/trinity/tdeio_locate.la
%{tde_prefix}/%{_lib}/trinity/tdeio_locate.so
%{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/locate/
%{tde_prefix}/share/services/locate.protocol
%{tde_prefix}/share/services/locater.protocol
%{tde_prefix}/share/services/rlocate.protocol
%{tde_prefix}/share/services/searchproviders/locate.desktop


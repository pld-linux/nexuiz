#
%define _ver	%(echo %{version} | tr -d .)
%define _ever	20091001
Summary:	nexuiz - engine for first-person shoter game
Summary(pl.UTF-8):	nexuiz - silnik do strzelaniny w pierwszej osobie
Name:		nexuiz
Version:	2.5.2
Release:	3
License:	GPL v2+
Group:		X11/Applications/Games
# extracted from: http://dl.sourceforge.net/nexuiz/%{name}-%{_ver}.zip
Source0:	enginesource%{_ever}.zip
# Source0-md5:	aa4e586e58e1c35a5e3ed76cc9348fbd
Source1:	%{name}-glx.desktop
Source2:	%{name}-sdl.desktop
Source3:	%{name}.png
# Source version of Nexuiz logo in inkspace svg format
Source4:	%{name}.svg
URL:		http://alientrap.org/nexuiz/
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires:	nexuiz-data = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nexuiz is a fast-paced, chaotic, and intense multiplayer first-person
shooter game, focused on providing basic, old style deathmatch. It is
extremely modder-friendly. Nexuiz is built on the power of the
Darkplaces engine, which is a heavily modified version of the original
Quake. Darkplaces features realtime lighting and stencil shadows,
bumpmapping, gloss, bloom, and totally rewritten network code that
supports up to 64 players on a single server.

%description -l pl.UTF-8
Nexuiz jest chaotyczną strzelaniną w pierwszej osobie, skupioną na
standardowym i klasycznym deathmatchu. Nexuiz jest bardzo przyjazny
dla moderów. Jest oparty na silniku Darkplaces, czyli mocno
zmodyfikowanej wersji oryginalnego silnika Quake. Darkplaces ma
całkowicie przepisany kod obsługi sieci, dzięki któremu mogą walczyć
64 osoby na pojedynczym serwerze.

%prep
%setup -q -n darkplaces
%{__sed} -i 's/-Wdeclaration-after-statement//; /strip /d' makefile.inc

%build
%{__make} -j1 nexuiz \
	CC="%{__cc}" \
	OPTIM_RELEASE="%{rpmcflags}" \
	LDFLAGS_RELEASE="%{rpmcflags} %{rpmldflags}" \
	DP_FS_BASEDIR="%{_datadir}/games/%{name}" \
	DP_LINK_TO_LIBJPEG=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}
install nexuiz-* $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

# remove junk
rm -f $RPM_BUILD_ROOT%{_bindir}/nexuiz-base-revision.txt $RPM_BUILD_ROOT%{_bindir}/nexuiz-engine-changes.diff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nexuiz-glx
%attr(755,root,root) %{_bindir}/nexuiz-sdl
%attr(755,root,root) %{_bindir}/nexuiz-dedicated
%{_desktopdir}/nexuiz*.desktop
%{_pixmapsdir}/%{name}.png
%{_pixmapsdir}/%{name}.svg

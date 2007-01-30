%define	_ver	%(echo %{version} | tr -d .)
Summary:	nexuiz - engine for first-person shoter game
Summary(pl):	nexuiz - silnik do strzelaniny w pierwszej osobie
Name:		nexuiz
Version:	2.2.3
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/nexuiz/%{name}-%{_ver}.zip
# Source0-md5:	953fda1555fc1f9ca040bdbb797eb0fd
URL:		http://nexuiz.com/
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	sed
BuildRequires:	unzip
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

%description -l pl
Nexuiz jest chaotyczn± strzelanin± w pierwszej osobie, skupion± na
standardowym i klasycznym deathmatch'u. Nexuiz jest bardzo przyjezny
dla moderów. Jeste oparty na silniku Darkplaces, czyli mocno
zmodyfikowan± wersj± oryginalnego silnika Quake. Darkplaces ma
totalnie przepisany kod obs³ugi sieci, dziêki któremu mog± walczyæ 64
osoby na pojedynczym serwerze.

%prep
%setup -q -n Nexuiz
cd sources
%{__unzip} -o -qq enginesource20070123.zip
sed -i 's/-Wdeclaration-after-statement//; /strip /d' darkplaces/makefile.inc

%build
cd sources/darkplaces
%{__make} nexuiz \
	CC="%{__cc}" \
	OPTIM_RELEASE="%{rpmcflags}" \
	LDFLAGS_RELEASE="%{rpmcflags} %{rpmldflags}" \
	DP_FS_BASEDIR="%{_datadir}/games/%{name}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install sources/darkplaces/nexuiz-* $RPM_BUILD_ROOT%{_bindir}
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

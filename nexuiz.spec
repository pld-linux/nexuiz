Summary:	nexuiz - engine for first-person shoter game
Summary(pl):	nexuiz - silnik do strzelaniny w pierwszej osobie
Name:		nexuiz
Version:	223
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/nexuiz/%{name}-%{version}.zip
# Source0-md5:	953fda1555fc1f9ca040bdbb797eb0fd
Patch0:		%{name}-datadir.patch
URL:		http://nexuiz.com/
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	unzip
Requires:	nexuiz-data
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

%package data
Summary:	Data files for nexuiz
Summary(pl):	Pliki gry nexuiz
Group:		Applications/Games
BuildArch:	noarch

%description data
Data files with textures, sound etc for nexuiz.

%description data -l pl
Pliki z texturami, d¼wiêkami itd dla gry nexuiz.

%prep
%setup -q -n Nexuiz
cd sources
%{__unzip} -o -qq enginesource20070123.zip
sed -i s/-Wdeclaration-after-statement/#-Wdeclaration-after-statement/ darkplaces/makefile.inc
%patch0 -p0

%build
cd sources/darkplaces
%{__make}  nexuiz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/games/%{name}/data
install sources/darkplaces/nexuiz-* $RPM_BUILD_ROOT%{_bindir}
install data/* $RPM_BUILD_ROOT%{_datadir}/games/%{name}/data

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%files data
%defattr(644,root,root,755)
%{_datadir}/games/%{name}

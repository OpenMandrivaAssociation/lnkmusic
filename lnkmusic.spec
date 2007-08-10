Summary:	A new and cool interface for MPD
Name:		lnkmusic
Version:	0.1.9
Release:	%mkrel 1
License:	GPL
Group:		Sound
URL:		http://sourceforge.net/projects/lnkmusic/
Source0:	http://downloads.sourceforge.net/lnkmusic/%{name}-%{version}.tar.bz2
Requires:	gambas2-runtime >= 1.9.48,gambas2-runtime < 2.1,gambas2-gb-qt >= 1.9.48,gambas2-gb-qt < 2.1,gambas2-gb-form >= 1.9.48,gambas2-gb-form < 2.1,gambas2-gb-image >= 1.9.48,gambas2-gb-image < 2.1,gambas2-gb-net >= 1.9.48,gambas2-gb-net < 2.1,gambas2-gb-qt-ext >= 1.9.48,gambas2-gb-qt-ext < 2.1,gambas2-gb-settings >= 1.9.48,gambas2-gb-settings < 2.1
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This is a new and cool interface for MPD
(Music player daemon, www.musicpd.org).

It has some nice features like playlist sorting and a nice 
tray system that lets you control mpd by the tray tooltip 
without having to open the main window.The tag browser is 
amarok-like with an integrated search engine.

%prep
%setup -qn %{name}

%build
/usr/bin/gbc2 -a -t -p 
gba2

%install
install -d %{buildroot}/%{_bindir}
install -p lnkmusic.gambas %{buildroot}/%{_bindir}/lnkmusic
install -d %{buildroot}/%{_miconsdir}
install -d %{buildroot}/%{_iconsdir}
install -d %{buildroot}/%{_liconsdir}
install -p .icon/16.png %{buildroot}/%{_miconsdir}/lnkmusic.png
install -p .icon/32.png %{buildroot}/%{_iconsdir}/lnkmusic.png
install -p .icon/48.png %{buildroot}/%{_liconsdir}/lnkmusic.png
install -d %{buildroot}/%{_datadir}/applications

cat << EOF > %{buildroot}/%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=lnkmusic
Comment=A nice frontend for MPD
Exec=%{_bindir}/lnkmusic
Icon=lnkmusic.png
Terminal=false
Type=Application
StartupNotify=true
Categories=Audio;AudioVideo;
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/lnkmusic
%{_miconsdir}/lnkmusic.png
%{_iconsdir}/lnkmusic.png
%{_liconsdir}/lnkmusic.png
%{_datadir}/applications/%{name}.desktop

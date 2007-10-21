Summary:	A new and cool interface for MPD
Name:		lnkmusic
Version:	0.2.22
Release:	%mkrel 1
License:	GPL
Group:		Sound
URL:		http://sourceforge.net/projects/lnkmusic/
Source0:	http://downloads.sourceforge.net/lnkmusic/%{name}-%{version}.tar.gz
BuildRequires:	gambas2-devel >= 1.9.48
BuildRequires:	gambas2-runtime >= 1.9.48
BuildRequires:	gambas2-gb-qt >= 1.9.48
BuildRequires:	gambas2-gb-form >= 1.9.48
BuildRequires:	gambas2-gb-image >= 1.9.48
BuildRequires:	gambas2-gb-net >= 1.9.48
BuildRequires:	gambas2-gb-qt-ext >= 1.9.48
BuildRequires:	gambas2-gb-settings >= 1.9.48
BuildArch:	noarch
ExclusiveArch:	%{ix86}
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
gbc2 -a -t -p 
gba2

%install
install -d %{buildroot}/%{_bindir}
install -p lnkmusic.gambas %{buildroot}/%{_bindir}/lnkmusic
install -d %{buildroot}/%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert Images/logo2.png -resize 16x16 %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/lnkmusic.png
convert Images/logo2.png -resize 32x32 %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/lnkmusic.png
convert Images/logo2.png -resize 48x48 %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/lnkmusic.png
install -d %{buildroot}/%{_datadir}/applications

cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Name=lnkmusic
Comment=A nice frontend for MPD
Exec=%{_bindir}/lnkmusic
Icon=lnkmusic
Terminal=false
Type=Application
StartupNotify=true
Categories=Audio;AudioVideo;
EOF

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/lnkmusic
%{_iconsdir}/hicolor/*/apps/lnkmusic.png
%{_datadir}/applications/%{name}.desktop

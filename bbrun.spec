Summary:	Run window for Blackbox
Name:		bbrun
Version:	1.6
Release:	11
License:	GPL
Group: 		Toys
Url:		http://www.darkops.net/bbrun
Source: 	http://www.darkops.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		bbrun-1.6-linkage.patch
BuildRequires:	xpm-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xpm)

%description
bbrun is a run window for Blackbox with dropdown history list.

%prep
%setup -q
%patch0 -p1
find . -perm 0600 | xargs chmod 0644

%build
cd bbrun
%make

%install
install -d %{buildroot}%{_bindir}
install bbrun/bbrun %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=BB Run
Comment=BlackBox Run Window
Exec=%{_bindir}/%{name}
Icon=office_accessories_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Office-Accessories;Office;Utility;
EOF

%files
%doc README Changelog COPYING CREDITS
%{_bindir}/*
%{_datadir}/applications/mandriva-%{name}.desktop


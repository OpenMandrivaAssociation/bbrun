%define name		bbrun
%define version		1.6
%define release		%mkrel 9

Summary:	Run window for Blackbox
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Toys
Url:		http://www.darkops.net/bbrun
Source: 	http://www.darkops.net/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:	xpm-devel gtk+2-devel


%description
bbrun is a run window for Blackbox with dropdown history list.

%prep

%setup -q

%build
cd bbrun
%make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -s  bbrun/bbrun $RPM_BUILD_ROOT%{_bindir}


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=BB Run
Comment=BlackBox Run Window
Exec=%{_bindir}/%{name} 
Icon=office_accessories_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Office-Accessories;Office;Utility
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,0755) 
%_bindir/*
%{_datadir}/applications/mandriva-%{name}.desktop
%doc README Changelog COPYING CREDITS


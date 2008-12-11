%define name	keyfuzz
%define version	0.2
%define release %mkrel 4

Name: 	 	%{name}
Summary: 	Keycode translator for multimedia keyboards
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://0pointer.de/lennart/projects/keyfuzz/
License:	GPL
Group:		System/Configuration/Hardware
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	imagemagick
BuildRequires:  lynx

%description
You may use keyfuzz to manipulate the scancode/keycode translation tables of
keyboard drivers supporting the Linux input layer API (as included in Linux
2.6). This is useful for fixing the translation tables of multimedia keyboards
or laptop keyboards with special keys. keyfuzz is not a daemon like Gnome acme
which reacts on special hotkeys but a tool to make non-standard keyboards
compatible with such daemons. keyfuzz should be run once at boot time, the
modifications it makes stay active after the tool quits until reboot. keyfuzz
does not interact directly with XFree86. However, newer releases of the latter
(4.1 and above) rely on the Linux input API, so they take advantage of the
fixed translation tables.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README doc/*.html doc/*.css
%{_sbindir}/%name
%{_mandir}/man8/*
%{_sysconfdir}/init.d/*
%{_sysconfdir}/%name




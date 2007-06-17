%define	name	xmailbox
%define	version	2.5
%define	release	%mkrel 22

Summary:	An X Window System utility which notifies you of new mail
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MIT
Group:		Networking/Mail
BuildRequires:	libx11-devel libxext-devel libxaw-devel libxmu-devel libxt-devel xpm-devel imake
Source0:	ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tar.bz2
Patch1:		xmailbox-2.2-xpm.patch
Patch2:		xmailbox-2.4-glibc.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The xmailbox program is an X Window System program which notifies you
when mail arrives.  Xmailbox is similar to the xbiff program, but it
offers more features and notification options.

Install the xmailbox package if you'd like a graphical program for X
which will notify you when new mail arrives.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
xmkmf
%make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig

%{makeinstall_std} install.man

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Xmailbox
Comment=Mail notifier
Exec=%{_bindir}/%{name} 
Icon=mail_section.png
Terminal=false
Type=Application
StartupNotify=true
Categories=Utility;Network;Email;X-MandrivaLinux-Internet-Mail;
EOF

#(peroyvind) get rid of unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/xmailbox
%{_mandir}/man1/xmailbox.1*
%config(noreplace) %{_sysconfdir}/X11/app-defaults/XMailbox
%{_datadir}/applications/mandriva-%{name}.desktop


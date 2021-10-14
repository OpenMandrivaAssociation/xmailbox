Summary:	An X Window System utility which notifies you of new mail
Name:		xmailbox
Version:	2.5
Release:	41
License:	MIT
Group:		Networking/Mail
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	xaw-devel
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	imake
Source0:	ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tar.bz2
Patch1:		xmailbox-2.2-xpm.patch
Patch2:		xmailbox-2.4-glibc.patch

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
%setup_compile_flags
xmkmf
%make CDEBUGFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_sysconfdir}/X11/wmconfig

%{makeinstall_std} install.man

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Xmailbox
Comment=Mail notifier
Exec=%{_bindir}/%{name} 
Icon=mail_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Utility;Network;Email;X-MandrivaLinux-Internet-Mail;
EOF

#(peroyvind) get rid of unpackaged files
rm -f %{buildroot}%{_prefix}/lib/X11/app-defaults

%files
%doc README
%{_bindir}/xmailbox
%{_mandir}/man1/xmailbox.1*
%{_datadir}/X11/app-defaults/XMailbox
%{_datadir}/applications/mandriva-%{name}.desktop

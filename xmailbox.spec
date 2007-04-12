%define	name	xmailbox
%define	version	2.5
%define	release	21mdk

Summary:	An X Window System utility which notifies you of new mail
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MIT
Group:		Networking/Mail
BuildRequires:	XFree86-devel xpm-devel X11
Source0:	ftp://ftp.x.org/contrib/applications/%{name}-%{version}.tar.bz2
Source11:	%{name}-16.png
Source12:	%{name}-32.png
Source13:	%{name}-48.png
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

#menu and icons
install -d $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}): needs="X11" \
icon="mail_section.png" \
section="Internet/Mail" \
title="Xmailbox" \
longtitle="Mail notifier" \
command="%{_prefix}/X11R6/bin/%{name}"
EOF

#(peroyvind) get rid of unpackaged files
rm -f $RPM_BUILD_ROOT%{_prefix}/X11R6/lib/X11/app-defaults

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_prefix}/X11R6/bin/xmailbox
%{_prefix}/X11R6/man/man1/xmailbox.1*
%{_prefix}/X11R6/lib/X11/doc/html/xmailbox.1.html
%config(noreplace) %{_sysconfdir}/X11/app-defaults/XMailbox
%{_menudir}/%{name}


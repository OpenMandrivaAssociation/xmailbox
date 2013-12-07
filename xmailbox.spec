%define	name	xmailbox
%define	version	2.5

Summary:	An X Window System utility which notifies you of new mail
Name:		%{name}
Version:	%{version}
Release:	33
License:	MIT
Group:		Networking/Mail
BuildRequires:	pkgconfig(x11) libxext-devel libxaw-devel libxmu-devel libxt-devel xpm-devel imake
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
xmkmf
%make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig

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
rm -f $RPM_BUILD_ROOT%{_prefix}/lib/X11/app-defaults

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
%defattr(-,root,root)
%doc README
%{_bindir}/xmailbox
%{_mandir}/man1/xmailbox.1*
%config(noreplace) %{_sysconfdir}/X11/app-defaults/XMailbox
%{_datadir}/applications/mandriva-%{name}.desktop



%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5-29mdv2011.0
+ Revision: 671341
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5-28mdv2011.0
+ Revision: 608219
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5-27mdv2010.1
+ Revision: 524453
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.5-26mdv2009.1
+ Revision: 350983
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.5-25mdv2009.0
+ Revision: 226059
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 2.5-24mdv2008.1
+ Revision: 179496
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill explicit icon extension
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Sun Jun 17 2007 Adam Williamson <awilliamson@mandriva.org> 2.5-23mdv2008.0
+ Revision: 40558
- trim BuildRequires; new X layout; XDG menu; drop ugly icon; rebuild for new era


* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.5-21mdk
- Rebuild

* Sat Dec 25 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.5-20mdk
- fix buildrequires for real

* Sat Dec 25 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.5-19mdk
- fix buildrequires
- fix summary-ended-with-dot

* Wed Feb 18 2004 David Baudens <baudens@mandrakesoft.com> 2.5-18mdk
- Fix menu

* Tue Jan 27 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.5-17mdk
- get rid of unpackaged symlink
- drop prefix tag
- cosmetics

* Sun May 04 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.5-16mdk
- rebuild for rpm 4.2
- fix unpackaged files
- menu in spec
- png icons

* Sat Aug 11 2001 Jesse Kuang <kjx@mandrakesoft.com> 2.5-15mdk
- rebuilt for cooker

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.5-14mdk
- automatically added BuildRequires

* Fri Jul 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.5-13mdk
- BM

* Thu May 04 2000 Vincent Saugey <vince@mandrakesoft.com> 2.5-12mdk
- Remove menu entry

* Fri Apr 28 2000 Daouda Lo <daouda@mandrakesoft.com> 2.5-11mdk
- some changes to spec files
- add icons (entries without icons are very ugly ;-)

* Fri Mar 31 2000 DindinX <odin@mandrakesoft.com> 2.5-10mdk
- Spec and group fixes
- Menu

* Fri Nov 05 1999 Damien Krotkine <damien.mandrakesoft.com>
- Mandrake release

* Thu May 06 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 7)

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- build for 6.0

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed May 06 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- updated wmconfig Group line

* Wed Oct 29 1997 Marc Ewing <marc@redhat.com>
- wmconfig

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc


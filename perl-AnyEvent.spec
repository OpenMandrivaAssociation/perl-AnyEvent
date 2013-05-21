%define pkgname AnyEvent
%define filelist %{pkgname}-%{version}-filelist
%define maketest 1
%define upstream_version 7.04

Name:		perl-%{pkgname}
Summary:	Provide framework for multiple event loops
Version:	%perl_convert_version %{upstream_version}
Release:	2
Epoch:		3
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/~mlehmann/AnyEvent/
Source0:	http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/AnyEvent-%upstream_version.tar.gz
Source1:	perl-AnyEvent.rpmlintrc
BuildRequires:	perl-devel
BuildRequires:	perl-Event

%description
AnyEvent - provide framework for multiple event loops
Event, Glib, Tk, Perl, - various supported event loops.

%package EV
Group:		Development/Perl
Summary:	Provide framework for multiple event loops - EV integration

%description EV
AnyEvent - provide framework for multiple event loops
EV event loop integration.

%package Event-Lib
Group:		Development/Perl
Summary:	Provide framework for multiple event loops - Event::Lib integration

%description Event-Lib
AnyEvent - provide framework for multiple event loops
Event::Lib event loop integration.

%package Tk
Group:		Development/Perl
Summary:	Provide framework for multiple event loops - Tk integration

%description Tk
AnyEvent - provide framework for multiple event loops
Tk event loop integration.

%package POE
Group:		Development/Perl
Summary:	Provide framework for multiple event loops - POE integration

%description POE
AnyEvent - provide framework for multiple event loops
POE event loop integration.

%package IOAsync
Group:		Development/Perl
Summary:	Provide framework for multiple event loops - IO::Async integration

%description IOAsync
AnyEvent - provide framework for multiple event loops
IO::Async event loop integration.

%package Irssi
Group:		Development/Perl
Summary:	Provide framework for multiple event loops - Irssi integration

%description Irssi
AnyEvent - provide framework for multiple event loops
Irssi event loop integration.


%prep
%setup -q -n %{pkgname}-%{upstream_version}
chmod -R u+w %{_builddir}/%{pkgname}-%{upstream_version}

%build
grep -rsl '^#!.*perl' . |
grep -v '.bak$' |xargs --no-run-if-empty \
%__perl -MExtUtils::MakeMaker -e 'MY->fixin(@ARGV)'
CFLAGS="$RPM_OPT_FLAGS"
%{__perl} Makefile.PL `%{__perl} -MExtUtils::MakeMaker -e ' print qq|PREFIX=%{buildroot}%{_prefix}| if \$ExtUtils::MakeMaker::VERSION =~ /5\.9[1-6]|6\.0[0-5]/ '` INSTALLDIRS=vendor
%{make}

%check
make test

%install
%{makeinstall} `%{__perl} -MExtUtils::MakeMaker -e ' print \$ExtUtils::MakeMaker::VERSION <= 6.05 ? qq|PREFIX=%{buildroot}%{_prefix}| : qq|DESTDIR=%{buildroot}| '`

# remove special files
find %{buildroot} -name "perllocal.pod" \
    -o -name ".packlist"                \
    -o -name "*.bs"                     \
    |xargs -i rm -f {}

# no empty directories
find %{buildroot}%{_prefix}             \
    -type d -depth                      \
    -exec rmdir {} \; 2>/dev/null

#we don't have perl-Qt anymore:
rm -f %{buildroot}%{perl_vendorarch}/AnyEvent/Impl/Qt.pm
rm -f %{buildroot}%{_mandir}/man3/AnyEvent::Impl::Qt*
#we don't have perl-FLTK (yet):
rm -f %{buildroot}%{perl_vendorarch}/AnyEvent/Impl/FLTK.pm
rm -f %{buildroot}%{_mandir}/man3/AnyEvent::Impl::FLTK*
#only for Mac:
rm -f %{buildroot}%{perl_vendorarch}/AnyEvent/Impl/Cocoa.pm
rm -f %{buildroot}%{_mandir}/man3/AnyEvent::Impl::Cocoa*

%files
%doc README Changes
%{perl_vendorarch}/AE.pm
%{perl_vendorarch}/AnyEvent.pm
%dir %{perl_vendorarch}/AnyEvent
%dir %{perl_vendorarch}/AnyEvent/Impl
%{perl_vendorarch}/AnyEvent/Debug.pm
%{perl_vendorarch}/AnyEvent/DNS.pm
%{perl_vendorarch}/AnyEvent/FAQ.pod
%{perl_vendorarch}/AnyEvent/Handle.pm
%{perl_vendorarch}/AnyEvent/Log.pm
%{perl_vendorarch}/AnyEvent/Loop.pm
%{perl_vendorarch}/AnyEvent/Socket.pm
%{perl_vendorarch}/AnyEvent/Strict.pm
%{perl_vendorarch}/AnyEvent/Intro.pod
%{perl_vendorarch}/AnyEvent/TLS.pm
%{perl_vendorarch}/AnyEvent/Util.pm
%{perl_vendorarch}/AnyEvent/Util/
%{perl_vendorarch}/AnyEvent/IO.pm
%{perl_vendorarch}/AnyEvent/IO/
%{perl_vendorarch}/AnyEvent/Impl/Event.pm
%{perl_vendorarch}/AnyEvent/Impl/Glib.pm
%{perl_vendorarch}/AnyEvent/Impl/Perl.pm
%{perl_vendorarch}/AnyEvent/constants.pl
%{_mandir}/man3/AE.3pm*
%{_mandir}/man3/AnyEvent.3pm*
%{_mandir}/man3/AnyEvent::Debug*
%{_mandir}/man3/AnyEvent::DNS*
%{_mandir}/man3/AnyEvent::FAQ*
%{_mandir}/man3/AnyEvent::Handle*
%{_mandir}/man3/AnyEvent::Socket.*
%{_mandir}/man3/AnyEvent::Strict.*
%{_mandir}/man3/AnyEvent::Util.*
%{_mandir}/man3/AnyEvent::Intro.*
%{_mandir}/man3/AnyEvent::IO*
%{_mandir}/man3/AnyEvent::Impl::Event.*
%{_mandir}/man3/AnyEvent::Impl::Glib.*
%{_mandir}/man3/AnyEvent::Impl::Perl*
%{_mandir}/man3/AnyEvent::Log.*
%{_mandir}/man3/AnyEvent::Loop.*
%{_mandir}/man3/AnyEvent::TLS*

%files EV
%{perl_vendorarch}/AnyEvent/Impl/EV.pm
%{_mandir}/man3/AnyEvent::Impl::EV.3pm*

%files Event-Lib
%{perl_vendorarch}/AnyEvent/Impl/EventLib.pm
%{_mandir}/man3/AnyEvent::Impl::EventLib.3pm*

%files Tk
%{perl_vendorarch}/AnyEvent/Impl/Tk.pm
%{_mandir}/man3/AnyEvent::Impl::Tk*

%files POE
%{perl_vendorarch}/AnyEvent/Impl/POE.pm
%{_mandir}/man3/AnyEvent::Impl::POE*

%files IOAsync
%{perl_vendorarch}/AnyEvent/Impl/IOAsync.pm
%{_mandir}/man3/AnyEvent::Impl::IOAsync*

%files Irssi
%{perl_vendorarch}/AnyEvent/Impl/Irssi.pm
%{_mandir}/man3/AnyEvent::Impl::Irssi*


%changelog
* Wed Feb 01 2012 Götz Waschk <waschk@mandriva.org> 3:6.140.0-1
+ Revision: 770420
- update to new version 6.14

* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3:6.130.0-7
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Jan 13 2012 Götz Waschk <waschk@mandriva.org> 3:6.130.0-1
+ Revision: 760594
- update to new version 6.13

* Wed Dec 14 2011 Götz Waschk <waschk@mandriva.org> 3:6.120.0-1
+ Revision: 740974
- new version

* Wed Nov 23 2011 Götz Waschk <waschk@mandriva.org> 3:6.110.0-1
+ Revision: 732757
- update to new version 6.11

* Thu Oct 06 2011 Götz Waschk <waschk@mandriva.org> 3:6.100.0-1
+ Revision: 703244
- update to new version 6.1

* Tue Aug 30 2011 Götz Waschk <waschk@mandriva.org> 3:6.20.0-1
+ Revision: 697446
- remove unpackaged files, add new ones
- update to new version 6.02

* Fri May 13 2011 Götz Waschk <waschk@mandriva.org> 3:5.340.0-1
+ Revision: 674081
- update to new version 5.34

* Mon Jan 24 2011 Götz Waschk <waschk@mandriva.org> 3:5.310.0-1
+ Revision: 632475
- update to new version 5.31

* Sat Jan 01 2011 Götz Waschk <waschk@mandriva.org> 3:5.300.0-1mdv2011.0
+ Revision: 627052
- new version
- no more noarch package

* Mon Dec 06 2010 Götz Waschk <waschk@mandriva.org> 3:5.290.0-1mdv2011.0
+ Revision: 611944
- update to new version 5.29

* Thu Oct 14 2010 Götz Waschk <waschk@mandriva.org> 3:5.280.0-1mdv2011.0
+ Revision: 585582
- new version
- update file list

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 3:5.271.0-1mdv2011.0
+ Revision: 550298
- update to new version 5.271

* Thu Apr 29 2010 Götz Waschk <waschk@mandriva.org> 3:5.261.0-1mdv2010.1
+ Revision: 540767
- update to new version 5.261

* Mon Apr 12 2010 Götz Waschk <waschk@mandriva.org> 3:5.260.0-1mdv2010.1
+ Revision: 533663
- update to new version 5.26

* Sat Mar 13 2010 Götz Waschk <waschk@mandriva.org> 3:5.251.0-1mdv2010.1
+ Revision: 518718
- new version
- update file list

  + Jérôme Quelin <jquelin@mandriva.org>
    - update to 5.251

* Wed Jan 06 2010 Götz Waschk <waschk@mandriva.org> 3:5.240.0-1mdv2010.1
+ Revision: 486563
- update to new version 5.24

* Mon Dec 21 2009 Götz Waschk <waschk@mandriva.org> 3:5.230.0-1mdv2010.1
+ Revision: 480555
- new version
- update file list

* Sun Dec 06 2009 Jérôme Quelin <jquelin@mandriva.org> 3:5.220.0-1mdv2010.1
+ Revision: 474073
- update to 5.22

* Sat Nov 21 2009 Jérôme Quelin <jquelin@mandriva.org> 3:5.210.0-1mdv2010.1
+ Revision: 467872
- update to 5.21

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 3:5.202.0-1mdv2010.1
+ Revision: 460761
- update to new version 5.202

* Wed Sep 30 2009 Jérôme Quelin <jquelin@mandriva.org> 3:5.201.0-1mdv2010.0
+ Revision: 451157
- update to 5.201

* Tue Sep 15 2009 Jérôme Quelin <jquelin@mandriva.org> 3:5.200.0-1mdv2010.0
+ Revision: 442658
- update to 5.2

* Wed Sep 02 2009 Götz Waschk <waschk@mandriva.org> 3:5.120.0-1mdv2010.0
+ Revision: 424326
- update to new version 5.12
- disable Qt binding

* Sun Aug 23 2009 Götz Waschk <waschk@mandriva.org> 3:5.112.0-1mdv2010.0
+ Revision: 419889
- update to new version 5.112

* Thu Aug 20 2009 Götz Waschk <waschk@mandriva.org> 3:5.111.0-1mdv2010.0
+ Revision: 418523
- new version
- update file list

* Wed Jul 29 2009 Götz Waschk <waschk@mandriva.org> 3:4.881.0-1mdv2010.0
+ Revision: 402938
- new version
- add Irssi implementation

* Fri Jul 24 2009 Götz Waschk <waschk@mandriva.org> 3:4.860.0-2mdv2010.0
+ Revision: 399183
- rebuild for missing packages

* Thu Jul 23 2009 Götz Waschk <waschk@mandriva.org> 3:4.860.0-1mdv2010.0
+ Revision: 398777
- new version

* Sun Jul 19 2009 Götz Waschk <waschk@mandriva.org> 3:4.850.0-1mdv2010.0
+ Revision: 397467
- new version

* Sun Jul 12 2009 Götz Waschk <waschk@mandriva.org> 3:4.820.0-1mdv2010.0
+ Revision: 395093
- new version

* Fri Jul 10 2009 Götz Waschk <waschk@mandriva.org> 3:4.810.0-1mdv2010.0
+ Revision: 394167
- new version

* Wed Jul 08 2009 Götz Waschk <waschk@mandriva.org> 3:4.800.0-1mdv2010.0
+ Revision: 393443
- new version
- update file list

* Sun Jul 05 2009 Götz Waschk <waschk@mandriva.org> 3:4.451.0-1mdv2010.0
+ Revision: 392602
- update to new version 4.451

* Wed Jul 01 2009 Götz Waschk <waschk@mandriva.org> 3:4.450.0-1mdv2010.0
+ Revision: 391166
- new version

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 3:4.420.0-1mdv2010.0
+ Revision: 390460
- new version
- add IO::Async wrapper

* Mon Jun 08 2009 Götz Waschk <waschk@mandriva.org> 3:4.411.0-1mdv2010.0
+ Revision: 384004
- update to new version 4.411
- use the right version macro

* Mon May 18 2009 Götz Waschk <waschk@mandriva.org> 3:4.410.0-1mdv2010.0
+ Revision: 376914
- new version
- remove the macro definition again

* Fri May 08 2009 Götz Waschk <waschk@mandriva.org> 3:4.400.0-1mdv2010.0
+ Revision: 373387
- add definition of perl_convert_version
- new version
- use perl version macro

* Fri Apr 24 2009 Götz Waschk <waschk@mandriva.org> 3:4.35-1mdv2010.0
+ Revision: 368986
- new version

* Thu Feb 19 2009 Götz Waschk <waschk@mandriva.org> 3:4.34-1mdv2009.1
+ Revision: 342890
- new version

* Tue Jan 13 2009 Götz Waschk <waschk@mandriva.org> 2:4.331-1mdv2009.1
+ Revision: 328930
- update to new version 4.331

* Fri Nov 28 2008 Götz Waschk <waschk@mandriva.org> 2:4.33-1mdv2009.1
+ Revision: 307389
- update to new version 4.33

* Wed Nov 12 2008 Götz Waschk <waschk@mandriva.org> 2:4.32-1mdv2009.1
+ Revision: 302428
- update to new version 4.32

* Mon Nov 03 2008 Götz Waschk <waschk@mandriva.org> 2:4.31-1mdv2009.1
+ Revision: 299373
- new version
- fix URL
- reenable Qt binding

* Thu Aug 14 2008 Götz Waschk <waschk@mandriva.org> 1:4.231-1mdv2009.0
+ Revision: 271727
- new version
- update file list

* Wed Jul 09 2008 Götz Waschk <waschk@mandriva.org> 1:4.151-2mdv2009.0
+ Revision: 232915
- drop perl-AnyEvent-Qt

* Tue Jun 10 2008 Götz Waschk <waschk@mandriva.org> 1:4.151-1mdv2009.0
+ Revision: 217358
- new version
- update file list

* Wed May 28 2008 Götz Waschk <waschk@mandriva.org> 1:4.05-1mdv2009.0
+ Revision: 212545
- new version
- drop Coro package
- add subpackages for Event-Lib, Qt and POE

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%{buildroot} on Pixel's request

* Wed Nov 28 2007 Götz Waschk <waschk@mandriva.org> 1:2.8-2mdv2008.1
+ Revision: 113642
- drop perl-AnyEvent-Coro-EV

* Mon Nov 26 2007 Götz Waschk <waschk@mandriva.org> 1:2.8-1mdv2008.1
+ Revision: 112049
- new version
- add new modules

* Sat Oct 27 2007 Götz Waschk <waschk@mandriva.org> 2.54-1mdv2008.1
+ Revision: 102572
- new version
- update URL
- update file list


* Fri Oct 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.02-2mdv2007.0
+ Revision: 73171
- import perl-AnyEvent-1.02-2mdv2007.0

* Fri Jul 21 2006 G�tz Waschk <waschk@mandriva.org> 1.02-1mdv2007.0
- Rebuild

* Tue Apr 04 2006 G�tz Waschk <waschk@mandriva.org> 1.02-1mdk
- initial package


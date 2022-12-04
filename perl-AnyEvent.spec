%define debug_package %{nil}

%define module AnyEvent

%define __noautoreq 'perl\\(AnyEvent:.*'

Name:		perl-%{module}
Summary:	Provide framework for multiple event loops
Version:	7.17
Release:	1
License:	Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/~mlehmann/AnyEvent/
Source0:	http://www.cpan.org/modules/by-module/AnyEvent/AnyEvent-%{version}.tar.gz
Source1:	perl-AnyEvent.rpmlintrc
BuildRequires:	perl-devel
BuildRequires:	perl-Event

# Optional dependencies we don't want to require
%global optional_deps                  AnyEvent::AIO
%global optional_deps %{optional_deps}|Cocoa::EventLoop
%global optional_deps %{optional_deps}|EV
%global optional_deps %{optional_deps}|Event
%global optional_deps %{optional_deps}|Event::Lib
%global optional_deps %{optional_deps}|EventLoop
%global optional_deps %{optional_deps}|FLTK
%global optional_deps %{optional_deps}|Glib
%global optional_deps %{optional_deps}|IO::AIO
%global optional_deps %{optional_deps}|IO::Async::Loop
%global optional_deps %{optional_deps}|Irssi
%global optional_deps %{optional_deps}|POE
%global optional_deps %{optional_deps}|Qt
%global optional_deps %{optional_deps}|Qt::isa
%global optional_deps %{optional_deps}|Qt::slots
%global optional_deps %{optional_deps}|Tk
%global optional_deps %{optional_deps}|UV

# Don't include optional dependencies
%global __requires_exclude ^perl[(](%{optional_deps})[)]


%description
AnyEvent - provide framework for multiple event loops
Event, Glib, Tk, Perl, - various supported event loops.

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

#---------------------------------------------------------------------------

%package EV
Group:		Development/Perl
Summary:	Provide framework for multiple event loops - EV integration

%description EV
AnyEvent - provide framework for multiple event loops
EV event loop integration.

%files EV
%{perl_vendorarch}/AnyEvent/Impl/EV.pm
%{_mandir}/man3/AnyEvent::Impl::EV.3pm*

#---------------------------------------------------------------------------

%package Event-Lib
Group:		Development/Perl
Summary:	Provide framework for multiple event loops - Event::Lib integration

%description Event-Lib
AnyEvent - provide framework for multiple event loops
Event::Lib event loop integration.

%files Event-Lib
%{perl_vendorarch}/AnyEvent/Impl/EventLib.pm
%{_mandir}/man3/AnyEvent::Impl::EventLib.3pm*

#---------------------------------------------------------------------------

%package Tk
Group:		Development/Perl
Summary:	Provide framework for multiple event loops - Tk integration

%description Tk
AnyEvent - provide framework for multiple event loops
Tk event loop integration.

%files Tk
%{perl_vendorarch}/AnyEvent/Impl/Tk.pm
%{_mandir}/man3/AnyEvent::Impl::Tk*

#---------------------------------------------------------------------------

%package POE
Group:		Development/Perl
Summary:	Provide framework for multiple event loops - POE integration

%description POE
AnyEvent - provide framework for multiple event loops
POE event loop integration.

%files POE
%{perl_vendorarch}/AnyEvent/Impl/POE.pm
%{_mandir}/man3/AnyEvent::Impl::POE*

#---------------------------------------------------------------------------

%package IOAsync
Group:		Development/Perl
Summary:	Provide framework for multiple event loops - IO::Async integration

%description IOAsync
AnyEvent - provide framework for multiple event loops
IO::Async event loop integration.

%files IOAsync
%{perl_vendorarch}/AnyEvent/Impl/IOAsync.pm
%{_mandir}/man3/AnyEvent::Impl::IOAsync*

#---------------------------------------------------------------------------

%package Irssi
Group:		Development/Perl
Summary:	Provide framework for multiple event loops - Irssi integration

%description Irssi
AnyEvent - provide framework for multiple event loops
Irssi event loop integration.

%files Irssi
%{perl_vendorarch}/AnyEvent/Impl/Irssi.pm
%{_mandir}/man3/AnyEvent::Impl::Irssi*

#---------------------------------------------------------------------------

%package UV
Group:      Development/Perl
Summary:    Provide framework for multiple event loops - UV integration

%description UV
AnyEvent - provide framework for multiple event loops
UV event loop integration

%files UV
%{perl_vendorarch}/AnyEvent/Impl/UV.pm
%_mandir/man3/AnyEvent::Impl::UV.3pm*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{module}-%{version}
#chmod -R u+w %{_builddir}/%{module}-%{version}

%build
grep -rsl '^#!.*perl' . |
grep -v '.bak$' |xargs --no-run-if-empty \
%__perl -MExtUtils::MakeMaker -e 'MY->fixin(@ARGV)'
CFLAGS="%{optflags}"
%{__perl} Makefile.PL `%{__perl} -MExtUtils::MakeMaker -e ' print qq|PREFIX=%{buildroot}%{_prefix}| if \$ExtUtils::MakeMaker::VERSION =~ /5\.9[1-6]|6\.0[0-5]/ '` INSTALLDIRS=vendor
%make_build

%install
%make_install `%{__perl} -MExtUtils::MakeMaker -e ' print \$ExtUtils::MakeMaker::VERSION <= 6.05 ? qq|PREFIX=%{buildroot}%{_prefix}| : qq|DESTDIR=%{buildroot}| '`

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


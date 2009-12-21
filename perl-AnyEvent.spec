%define pkgname AnyEvent
%define filelist %{pkgname}-%{version}-filelist
%define maketest 1
%define upstream_version 5.23

Name:      perl-%pkgname
Summary:   Provide framework for multiple event loops
Version:   %perl_convert_version %upstream_version
Release:   %mkrel 1
Epoch: 3
License:   Artistic
Group:     Development/Perl
URL:       http://search.cpan.org/~mlehmann/AnyEvent/
SOURCE:    http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/AnyEvent-%upstream_version.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%(id -u -n)
Buildarch: noarch
BuildRequires: perl-devel
BuildRequires: perl-Event

%description
AnyEvent - provide framework for multiple event loops
Event, Glib, Tk, Perl, - various supported event loops

%package EV
Group: Development/Perl
Summary: Provide framework for multiple event loops - EV integration
%description EV
AnyEvent - provide framework for multiple event loops
EV event loop integration

%package Event-Lib
Group: Development/Perl
Summary: Provide framework for multiple event loops - Event::Lib integration
%description Event-Lib
AnyEvent - provide framework for multiple event loops
Event::Lib event loop integration

%package Tk
Group: Development/Perl
Summary: Provide framework for multiple event loops - Tk integration
%description Tk
AnyEvent - provide framework for multiple event loops
Tk event loop integration

%package POE
Group: Development/Perl
Summary: Provide framework for multiple event loops - POE integration
%description POE
AnyEvent - provide framework for multiple event loops
POE event loop integration

%package IOAsync
Group: Development/Perl
Summary: Provide framework for multiple event loops - IO::Async integration
%description IOAsync
AnyEvent - provide framework for multiple event loops
IO::Async event loop integration

%package Irssi
Group: Development/Perl
Summary: Provide framework for multiple event loops - Irssi integration
%description Irssi
AnyEvent - provide framework for multiple event loops
Irssi event loop integration


%prep
%setup -q -n %{pkgname}-%{upstream_version} 
chmod -R u+w %{_builddir}/%{pkgname}-%{upstream_version}

%build
grep -rsl '^#!.*perl' . |
grep -v '.bak$' |xargs --no-run-if-empty \
%__perl -MExtUtils::MakeMaker -e 'MY->fixin(@ARGV)'
CFLAGS="$RPM_OPT_FLAGS"
%{__perl} Makefile.PL `%{__perl} -MExtUtils::MakeMaker -e ' print qq|PREFIX=%{buildroot}%{_prefix}| if \$ExtUtils::MakeMaker::VERSION =~ /5\.9[1-6]|6\.0[0-5]/ '` INSTALLDIRS=vendor
%{__make} 
%check
%{__make} test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

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
rm -f %buildroot%{perl_vendorlib}/AnyEvent/Impl/Qt.pm
rm -f %buildroot%_mandir/man3/AnyEvent::Impl::Qt*

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/AE.pm
%{perl_vendorlib}/AnyEvent.pm
%dir %{perl_vendorlib}/AnyEvent
%dir %{perl_vendorlib}/AnyEvent/Impl
%{perl_vendorlib}/AnyEvent/Debug.pm
%{perl_vendorlib}/AnyEvent/DNS.pm
%{perl_vendorlib}/AnyEvent/Handle.pm
%{perl_vendorlib}/AnyEvent/Socket.pm
%{perl_vendorlib}/AnyEvent/Strict.pm
%{perl_vendorlib}/AnyEvent/Intro.pod
%{perl_vendorlib}/AnyEvent/TLS.pm
%{perl_vendorlib}/AnyEvent/Util.pm
%{perl_vendorlib}/AnyEvent/Util/
%{perl_vendorlib}/AnyEvent/Impl/Event.pm
%{perl_vendorlib}/AnyEvent/Impl/Glib.pm
%{perl_vendorlib}/AnyEvent/Impl/Perl.pm
%_mandir/man3/AE.3pm*
%_mandir/man3/AnyEvent.3pm*
%_mandir/man3/AnyEvent::Debug*
%_mandir/man3/AnyEvent::DNS*
%_mandir/man3/AnyEvent::Handle*
%_mandir/man3/AnyEvent::Socket.*
%_mandir/man3/AnyEvent::Strict.*
%_mandir/man3/AnyEvent::Util.*
%_mandir/man3/AnyEvent::Intro.*
%_mandir/man3/AnyEvent::Impl::Event.*
%_mandir/man3/AnyEvent::Impl::Glib.*
%_mandir/man3/AnyEvent::Impl::Perl*
%_mandir/man3/AnyEvent::TLS*



%files EV
%defattr(-,root,root)
%{perl_vendorlib}/AnyEvent/Impl/EV.pm
%_mandir/man3/AnyEvent::Impl::EV.3pm*

%files Event-Lib
%defattr(-,root,root)
%{perl_vendorlib}/AnyEvent/Impl/EventLib.pm
%_mandir/man3/AnyEvent::Impl::EventLib.3pm*

%files Tk
%defattr(-,root,root)
%{perl_vendorlib}/AnyEvent/Impl/Tk.pm
%_mandir/man3/AnyEvent::Impl::Tk*

%files POE
%defattr(-,root,root)
%{perl_vendorlib}/AnyEvent/Impl/POE.pm
%_mandir/man3/AnyEvent::Impl::POE*

%files IOAsync
%defattr(-,root,root)
%{perl_vendorlib}/AnyEvent/Impl/IOAsync.pm
%_mandir/man3/AnyEvent::Impl::IOAsync*

%files Irssi
%defattr(-,root,root)
%{perl_vendorlib}/AnyEvent/Impl/Irssi.pm
%_mandir/man3/AnyEvent::Impl::Irssi*




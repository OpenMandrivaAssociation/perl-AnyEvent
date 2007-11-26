%define pkgname AnyEvent
%define filelist %{pkgname}-%{version}-filelist
%define NVR %{pkgname}-%{version}-%{release}
%define maketest 1

Name:      perl-%pkgname
Summary:   Provide framework for multiple event loops
Version:   2.8
Release:   %mkrel 1
Epoch: 1
License:   Artistic
Group:     Development/Perl
URL:       http://search.cpan.org/~mlehmann/AnyEvent/lib/AnyEvent.pm
SOURCE:    http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/AnyEvent-%version.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%(id -u -n)
Buildarch: noarch
BuildRequires: perl-devel
BuildRequires: perl-Event

%description
AnyEvent - provide framework for multiple event loops
Event, Coro, Glib, Tk - various supported event loops

%package Coro
Group: Development/Perl
Summary: Provide framework for multiple event loops - Coro integration
%description Coro
AnyEvent - provide framework for multiple event loops
Coro event loop integration

%package EV
Group: Development/Perl
Summary: Provide framework for multiple event loops - EV integration
%description EV
AnyEvent - provide framework for multiple event loops
EV event loop integration


%package Coro-EV
Group: Development/Perl
Summary: Provide framework for multiple event loops - Coro::EV integration
%description Coro-EV
AnyEvent - provide framework for multiple event loops
Coro::EV event loop integration


%package Tk
Group: Development/Perl
Summary: Provide framework for multiple event loops - Tk integration
%description Tk
AnyEvent - provide framework for multiple event loops
Tk event loop integration

%prep
%setup -q -n %{pkgname}-%{version} 
chmod -R u+w %{_builddir}/%{pkgname}-%{version}

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


%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/AnyEvent.pm
%dir %{perl_vendorlib}/AnyEvent
%dir %{perl_vendorlib}/AnyEvent/Impl
%{perl_vendorlib}/AnyEvent/Impl/Event.pm
%{perl_vendorlib}/AnyEvent/Impl/Glib.pm
%{perl_vendorlib}/AnyEvent/Impl/Perl.pm
%_mandir/man3/AnyEvent.3pm*

%files EV
%defattr(-,root,root)
%{perl_vendorlib}/AnyEvent/Impl/EV.pm
%_mandir/man3/AnyEvent::Impl::EV.3pm*

%files Coro
%defattr(-,root,root)
%{perl_vendorlib}/AnyEvent/Impl/Coro.pm

%files Coro-EV
%defattr(-,root,root)
%{perl_vendorlib}/AnyEvent/Impl/CoroEV.pm


%files Tk
%defattr(-,root,root)
%{perl_vendorlib}/AnyEvent/Impl/Tk.pm




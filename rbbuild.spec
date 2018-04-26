################################################################################

%define _root             /root
%define _bin              /bin
%define _sbin             /sbin
%define _srv              /srv
%define _logdir           %{_localstatedir}/log
%define _rundir           %{_localstatedir}/run
%define _lockdir          %{_localstatedir}/lock
%define _cachedir         %{_localstatedir}/cache
%define _loc_prefix       %{_prefix}/local
%define _loc_exec_prefix  %{_loc_prefix}
%define _loc_bindir       %{_loc_exec_prefix}/bin
%define _loc_libdir       %{_loc_exec_prefix}/%{_lib}
%define _loc_libexecdir   %{_loc_exec_prefix}/libexec
%define _loc_sbindir      %{_loc_exec_prefix}/sbin
%define _loc_bindir       %{_loc_exec_prefix}/bin
%define _loc_datarootdir  %{_loc_prefix}/share
%define _loc_includedir   %{_loc_prefix}/include
%define _rpmstatedir      %{_sharedstatedir}/rpm-state

################################################################################

%define install_dir       %{_loc_datarootdir}/%{name}
%define defs_dir          %{install_dir}/defs
%define blds_dir          %{install_dir}/blds

################################################################################

Summary:         Utility for compiling and installing different ruby versions
Name:            rbbuild
Version:         1.9.0
Release:         0%{?dist}
License:         EKOL
Vendor:          ESSENTIALKAOS
Group:           Development/Tools
URL:             https://github.com/essentialkaos/rbbuild

Source0:         https://source.kaos.st/%{name}/%{name}-%{version}.tar.bz2

BuildArch:       noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:        %{name}-defs
Requires:        bash p7zip patch gawk bc

Provides:        %{name} = %{version}-%{release}

################################################################################

%description
RBBuild provides a simple way to compile and install different versions of Ruby
on UNIX-like systems.

################################################################################

%prep
%setup -q

%build
%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_bindir}
install -dm 755 %{buildroot}%{blds_dir}

install -pm 755 rbdef %{buildroot}%{_bindir}/
install -pm 755 rbbuild %{buildroot}%{_bindir}/

cp blds/* %{buildroot}%{blds_dir}

chmod 644 %{buildroot}%{blds_dir}/*

%clean
rm -rf %{buildroot}

################################################################################

%files
%defattr(-,root,root,-)
%doc LICENSE.EN
%doc LICENSE.RU
%{_bindir}/rbbuild
%{_bindir}/rbdef
%{blds_dir}

################################################################################

%changelog
* Thu Apr 26 2018 Anton Novojilov <andy@essentialkaos.com> - 1.9.0-0
- Fixed bug with checking remote file status
- Improved proxy configuration
- Minor improvements

* Fri Apr 20 2018 Anton Novojilov <andy@essentialkaos.com> - 1.8.1-0
- Non-standard 'which' command replaced by 'command -v'

* Mon Apr 02 2018 Anton Novojilov <andy@essentialkaos.com> - 1.8.0-2
- Added bc to required dependencies

* Fri Feb 02 2018 Anton Novojilov <andy@essentialkaos.com> - 1.8.0-1
- Migrated from kaos.io to kaos.st

* Thu Dec 28 2017 Anton Novojilov <andy@essentialkaos.com> - 1.8.0-0
- [rbbuild] Fixed major bug with applying patches
- [rbbuild] Added 'ruby_bin' and 'java_bin' variables
- [rbbuild] Fixed minor bug with spinner
- [rbbuild] Fixed minor bug with checking remote source status
- [rbbuild] Fixed minor bug with sorting versions
- [rbbuild] Improved handling permission errors
- [rbbuild] Minor UI improvements
- [rbbuild] Code refactoring

* Tue Dec 12 2017 Anton Novojilov <andy@essentialkaos.com> - 1.7.1-0
- [rbdef|rbbuild] Code refactoring

* Sun Oct 08 2017 Anton Novojilov <andy@essentialkaos.com> - 1.7.0-0
- [rbdef|rbbuild] Print errors to stderr
- [rbbuild] Minor fixes
- [rbdef] Minor improvements

* Sun Jun 04 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.6-0
- [rbdef] Minor fixes

* Sat Apr 29 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.5-0
- [rbdef] Improved help output
- [rbbuild] Improved help output
- [rbdef] Code refactoring

* Mon Apr 24 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.4-0
- Arguments parser updated to v3 with fixed stderr output redirection for
  showArgWarn and showArgValWarn functions

* Wed Jan 25 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.3-0
- getThreadsNum now return 1 recommended thread if LA is too high

* Mon Jan 23 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.2-0
- Improved checking remote sources availability

* Fri Dec 30 2016 Anton Novojilov <andy@essentialkaos.com> - 1.6.1-1
- Minor fixes in rbdef

* Mon Dec 05 2016 Anton Novojilov <andy@essentialkaos.com> - 1.6.1-0
- Fixed bug with processing custom def files
- Fixed bug with -y/--yes option usage

* Sun Nov 27 2016 Anton Novojilov <andy@essentialkaos.com> - 1.6.0-0
- Code refactoring
- UI improvements

* Mon Sep 05 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.7-0
- Fixed ruby version output alignment

* Fri Jul 22 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.6-1
- Small fix for rbdef

* Wed Jul 13 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.6-0
- Improved listing

* Fri May 13 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.5-0
- Fixed bug with listing def files
- Improved listing

* Thu Apr 28 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.4-0
- Fixed typo in Mac OS name

* Tue Mar 01 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.3-0
- Fixed bug with ignoring checksums
- Fixed bug with showing error status codes

* Thu Aug 20 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.2-0
- Simple latest version install
- Minor improvements

* Tue May 19 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.1-0
- Improved defs listing

* Wed Jan 21 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.0-0
- Many improvements
- Fixed bug with dl-cache
- LA check before build process
- Using -cc and -cxx instead --compiler

* Wed Dec 10 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.4-0
- Custom compiler support for rubinius builder

* Tue Dec 09 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.3-0
- Added proxy support

* Thu Nov 13 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.2.1-0
- Small fix for verbose mode in rbx builder

* Thu Oct 30 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.2-0
- Fixed bugs with quiet mode
- Minor improvements

* Wed Sep 03 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.1-0
- Small fixes

* Mon Sep 01 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.0-0
- Fixed bug with dependencies check
- Added openssl builder

* Fri Aug 01 2014 Anton Novojilov <andy@essentialkaos.com> - 1.3.1-0
- Default temporary path now is /var/tmp

* Thu Jul 03 2014 Anton Novojilov <andy@essentialkaos.com> - 1.3.0-0
- Notifications about finished maintenance period

* Wed Jul 02 2014 Anton Novojilov <andy@essentialkaos.com> - 1.2.2-0
- Improved compatibility with rbenv

* Tue Jul 01 2014 Anton Novojilov <andy@essentialkaos.com> - 1.2.1-1
- Minor fixes in rbdef

* Thu Apr 17 2014 Anton Novojilov <andy@essentialkaos.com> - 1.2.1-0
- Fixed minor bug with output redirect in jruby builder

* Wed Apr 16 2014 Anton Novojilov <andy@essentialkaos.com> - 1.2.0-0
- Improved build system
- Using shenx instead of shmin
- Improved def file listing

* Tue Apr 15 2014 Anton Novojilov <andy@essentialkaos.com> - 1.1.2-0
- Custom names can be used with rbenv

* Sun Apr 06 2014 Anton Novojilov <andy@essentialkaos.com> - 1.1.1-0
- Some improvements in rbdef

* Fri Aug 23 2013 Anton Novojilov <andy@essentialkaos.com> - 1.0.2-0
- Fixed major bug with CFLAGS processing
- Fixed bug in prefs file parsing in rbdef
- Fixed bug in failed build processing
- Some minor improvements

* Mon Aug  5 2013 Anton Novojilov <andy@essentialkaos.com> - 1.0.1-0
- Improved argument parsing
- Added shmin usage

* Tue Jul  2 2013 Anton Novojilov <andy@essentialkaos.com> - 1.0.0-0
- First public release

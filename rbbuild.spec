################################################################################

Summary:    Utility for compiling and installing different ruby versions
Name:       rbbuild
Version:    2.4.4
Release:    0%{?dist}
License:    Apache License, Version 2.0
Vendor:     ESSENTIAL KAOS
Group:      Development/Tools
URL:        https://kaos.sh/rbbuild

Source0:    https://source.kaos.st/%{name}/%{name}-%{version}.tar.bz2

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:   %{name}-defs >= 2
Requires:   bash zstd patch gawk bc git

Provides:   %{name} = %{version}-%{release}

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
install -dm 755 %{buildroot}%{_libexecdir}/%{name}

install -pm 755 rbdef %{buildroot}%{_bindir}/
install -pm 755 rbbuild %{buildroot}%{_bindir}/

cp -r libexec/* %{buildroot}%{_libexecdir}/%{name}/

%clean
rm -rf %{buildroot}

################################################################################

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/rbbuild
%{_bindir}/rbdef
%{_libexecdir}/%{name}

################################################################################

%changelog
* Fri Dec 06 2024 Anton Novojilov <andy@essentialkaos.com> - 2.4.4-0
- Improved options parsing

* Sat Aug 03 2024 Anton Novojilov <andy@essentialkaos.com> - 2.4.3-0
- Use all cores to build OpenSSL by default
- Removed 7zip support

* Sun Jun 09 2024 Anton Novojilov <andy@essentialkaos.com> - 2.4.2-0
- Improved automatic disabling of color output usage

* Tue Dec 12 2023 Anton Novojilov <andy@essentialkaos.com> - 2.4.1-0
- Fixed bug with listing versions
- Fixed railsexpress build

* Thu Nov 30 2023 Anton Novojilov <andy@essentialkaos.com> - 2.4.0-0
- Code refactoring

* Mon Aug 28 2023 Anton Novojilov <andy@essentialkaos.com> - 2.3.0-0
- Improve OpenSSL builder
- Added def file listing
- Improved help content

* Mon Apr 10 2023 Anton Novojilov <andy@essentialkaos.com> - 2.2.0-0
- Added --ignore-loadavg/-il option for ignoring check for high LA

* Mon Jan 23 2023 Anton Novojilov <andy@essentialkaos.com> - 2.1.0-0
- Gathering and printing information about rust version

* Fri Dec 30 2022 Anton Novojilov <andy@essentialkaos.com> - 2.0.0-0
- Brand new version rewritten from scratch
- Using zstandart compression by default
- Removed outdated builders
- Added def file validation
- Builders now remove all useless data

* Mon Dec 06 2021 Anton Novojilov <andy@essentialkaos.com> - 1.10.4-1
- Code refactoring

* Sun Dec 05 2021 Anton Novojilov <andy@essentialkaos.com> - 1.10.4-0
- Fixed bug with listing 3.x versions
- Code refactoring

* Mon Feb 08 2021 Anton Novojilov <andy@essentialkaos.com> - 1.10.3-0
- Do not use current working directory for download cache
- Use 0600 as default mode for all files in download cache

* Tue Jun 30 2020 Anton Novojilov <andy@essentialkaos.com> - 1.10.2-0
- Added check for noexec flag for temporary directory

* Fri Jun 19 2020 Anton Novojilov <andy@essentialkaos.com> - 1.10.1-0
- Improved TruffleRuby builder

* Wed Jun 17 2020 Anton Novojilov <andy@essentialkaos.com> - 1.10.0-0
- Added TruffleRuby support
- Improved UI

* Tue Mar 03 2020 Anton Novojilov <andy@essentialkaos.com> - 1.9.7-1
- Minor improvements for rbdef

* Wed Dec 04 2019 Anton Novojilov <andy@essentialkaos.com> - 1.9.7-0
- Removed handler for script errors

* Sat Nov 30 2019 Anton Novojilov <andy@essentialkaos.com> - 1.9.6-0
- Added handling of SCRIPT_DEBUG environment variable for enabling debug mode
- Added handler for script errors

* Thu Jun 06 2019 Anton Novojilov <andy@essentialkaos.com> - 1.9.5-0
- [rbbuild] Improved build process for patched versions of Ruby

* Tue Jan 15 2019 Anton Novojilov <andy@essentialkaos.com> - 1.9.4-0
- [rbbuild] Added DLDFLAGS fixer for ruby builder

* Fri Jan 04 2019 Anton Novojilov <andy@essentialkaos.com> - 1.9.3-0
- [rbbuild] Code refactoring
- [rbdef] Minor UI improvements

* Thu Oct 18 2018 Anton Novojilov <andy@essentialkaos.com> - 1.9.2-0
- [rbbuild] Minor UI improvements

* Sat Sep 29 2018 Anton Novojilov <andy@essentialkaos.com> - 1.9.1-0
- [rbbuild] Code refactoring

* Thu Apr 26 2018 Anton Novojilov <andy@essentialkaos.com> - 1.9.0-0
- Print info about system before build
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

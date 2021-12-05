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

%define install_dir       %{_loc_datarootdir}/rbbuild
%define defs_dir          %{install_dir}/defs
%define blds_dir          %{install_dir}/blds

################################################################################

Summary:         Def files for rbbuild utility
Name:            rbbuild-defs
Version:         1.10.7
Release:         0%{?dist}
License:         Apache License, Version 2.0
Vendor:          ESSENTIAL KAOS
Group:           Development/Tools
URL:             https://kaos.sh/rbbuild

BuildArch:       noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# perfecto:absolve
Source0:         %{name}-%{version}.tar.bz2

Requires:        rbbuild

################################################################################

%description
Def (definition) files for rbbuild utility.

################################################################################

%prep
%setup -q
%build

%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{defs_dir}

cp -P defs/* %{buildroot}%{defs_dir}

chmod 644 %{buildroot}%{defs_dir}/*

%clean
rm -rf %{buildroot}

################################################################################

%files
%defattr(-,root,root,-)
%{defs_dir}/*

################################################################################

%changelog
* Sun Dec 05 2021 Anton Novojilov <andy@essentialkaos.com> - 1.10.7-0
- Added 2.6.8-railsexpress
- Added 2.7.4-railsexpress
- Added 3.0.2-railsexpress
- Added 3.0.3
- Added 3.0.3-jemalloc
- Added jruby-9.2.20.0
- Added jruby-9.2.20.1
- Added jruby-9.3.0.0
- Added jruby-9.3.1.0
- Added jruby-9.3.2.0

* Wed Aug 25 2021 Anton Novojilov <andy@essentialkaos.com> - 1.10.6-0
- OpenSSL updated to 1.1.1l for 2.4.0 <-> 3.0.0
- Added truffleruby-21.0.2
- Added truffleruby-21.0.2.1

* Thu Jul 08 2021 Anton Novojilov <andy@essentialkaos.com> - 1.10.5-0
- Added 2.6.7-railsexpress
- Added 2.6.8
- Added 2.6.8-jemalloc
- Added 2.7.3-railsexpress
- Added 2.7.4
- Added 2.7.4-jemalloc
- Added 3.0.1-railsexpress
- Added 3.0.2
- Added 3.0.2-jemalloc
- Added jruby-9.2.18.0
- Added jruby-9.2.19.0
- Added truffleruby-21.0.1

* Wed Apr 07 2021 Anton Novojilov <andy@essentialkaos.com> - 1.10.4-0
- OpenSSL updated to 1.1.1k for 2.4.0 <-> 3.0.0
- Added 2.5.9
- Added 2.5.9-jemalloc
- Added 2.6.7
- Added 2.6.7-jemalloc
- Added 2.7.3
- Added 2.7.3-jemalloc
- Added 3.0.1
- Added 3.0.1-jemalloc
- Added jruby-9.2.15.0
- Added jruby-9.2.16.0
- Added jruby-9.2.17.0
- Added truffleruby-21.0.0.2

* Wed Feb 17 2021 Anton Novojilov <andy@essentialkaos.com> - 1.10.3-0
- OpenSSL updated to 1.1.1j for 2.4.0 <-> 3.0.0

* Sat Feb 06 2021 Anton Novojilov <andy@essentialkaos.com> - 1.10.2-0
- Added 2.7.2
- Added 2.7.2-jemalloc
- Added 2.7.2-railsexpress
- Added 3.0.0
- Added 3.0.0-jemalloc
- Added 3.0.0-railsexpress
- Added jruby-9.2.12.0
- Added jruby-9.2.13.0
- Added jruby-9.2.14.0
- Added truffleruby-20.2.0
- Added truffleruby-20.3.0
- Added truffleruby-21.0.0
- OpenSSL updated to 1.0.2u for 1.9.2 <-> 2.3.8
- OpenSSL updated to 1.1.1i for 2.4.0 <-> 2.7.1
- Added EOL dates for 2.3.x, 2.4.x, 2.5.x, jruby-9.0.x.x and jruby-9.1.x.x

* Fri Jun 19 2020 Anton Novojilov <andy@essentialkaos.com> - 1.10.1-0
- Added truffleruby-19.3.0
- Added truffleruby-19.3.0.2
- Added truffleruby-19.3.1

* Wed Jun 17 2020 Anton Novojilov <andy@essentialkaos.com> - 1.10.0-0
- Removed all versions of Maglev
- Removed all versions of MRuby
- Removed all versions of REE
- Removed all versions of Rubinius
- Removed all versions of Topaz Ruby
- Added truffleruby-19.3.2
- Added truffleruby-20.0.0
- Added truffleruby-20.1.0

* Wed Apr 08 2020 Anton Novojilov <andy@essentialkaos.com> - 1.9.11-0
- Added 2.7.1
- Added 2.7.1-jemalloc
- Added 2.7.1-railsexpress
- Added 2.6.6
- Added 2.6.6-jemalloc
- Added 2.6.6-railsexpress
- Added 2.5.8
- Added 2.5.8-jemalloc
- Added 2.5.8-railsexpress
- Added jruby-9.2.11.1
- Fixed jruby-9.2.11.0
- Fixed 2.7.0-railsexpress
- OpenSSL updated to 1.1.1f for 2.4.0 <-> 2.6.3

* Tue Mar 03 2020 Anton Novojilov <andy@essentialkaos.com> - 1.9.10-0
- Added 2.7.0
- Added 2.7.0-jemalloc
- Added 2.7.0-railsexpress
- Added jruby-9.2.10.0
- Added jruby-9.2.11.0

* Thu Oct 31 2019 Anton Novojilov <andy@essentialkaos.com> - 1.9.9-0
- Added 2.4.9
- Added 2.4.9-jemalloc
- Added 2.4.9-railsexpress
- Added 2.5.7
- Added 2.5.7-jemalloc
- Added 2.5.7-railsexpress
- Added 2.6.5
- Added 2.6.5-jemalloc
- Added 2.6.5-railsexpress
- Added jruby-9.2.9.0

* Sat Sep 21 2019 Anton Novojilov <andy@essentialkaos.com> - 1.9.8-0
- Added 2.4.6
- Added 2.4.6-jemalloc
- Added 2.4.6-railsexpress
- Added 2.4.7
- Added 2.4.7-jemalloc
- Added 2.5.6
- Added 2.5.6-jemalloc
- Added 2.5.6-railsexpress
- Added 2.6.3-railsexpress
- Added 2.6.4
- Added 2.6.4-jemalloc
- Added 2.6.4-railsexpress
- OpenSSL updated to 1.1.1d for 2.4.0 <-> 2.6.3
- OpenSSL updated to 1.0.2t for 1.9.2-p180 <-> 2.3.8

* Fri Aug 16 2019 Anton Novojilov <andy@essentialkaos.com> - 1.9.7-0
- Added jruby-9.2.8.0
- OpenSSL updated to 1.0.1u for 1.8.7-p302 <-> 1.8.7-p371

* Wed Jun 05 2019 Anton Novojilov <andy@essentialkaos.com> - 1.9.6-0
- Added 2.6.3
- Added 2.5.5-railsexpress
- Added jruby-9.2.7.0
- OpenSSL updated to 1.1.1c for 2.4.0 <-> 2.6.2
- OpenSSL updated to 1.0.2s for 1.9.2-p180 <-> 2.3.8

* Sat Mar 16 2019 Anton Novojilov <andy@essentialkaos.com> - 1.9.5-0
- Added 2.5.4
- Added 2.5.5
- Added 2.6.2
- Added 2.5.4-railsexpress
- Added 2.6.2-railsexpress
- Fixed 2.6.1-railsexpress
- Added 2.3.0-jemalloc
- Added 2.3.1-jemalloc
- Added 2.3.2-jemalloc
- Added 2.3.3-jemalloc
- Added 2.3.4-jemalloc
- Added 2.3.5-jemalloc
- Added 2.3.6-jemalloc
- Added 2.3.7-jemalloc
- Added 2.3.8-jemalloc
- Added 2.4.0-jemalloc
- Added 2.4.1-jemalloc
- Added 2.4.2-jemalloc
- Added 2.4.3-jemalloc
- Added 2.4.4-jemalloc
- Added 2.4.5-jemalloc
- Added 2.5.0-jemalloc
- Added 2.5.1-jemalloc
- Added 2.5.2-jemalloc
- Added 2.5.3-jemalloc
- Added 2.5.4-jemalloc
- Added 2.5.5-jemalloc
- Added 2.6.0-jemalloc
- Added 2.6.1-jemalloc
- Added 2.6.2-jemalloc

* Tue Feb 26 2019 Anton Novojilov <andy@essentialkaos.com> - 1.9.4-0
- Added 2.6.1
- Added 2.6.1-railsexpress
- Added jruby-9.2.6.0

* Mon Jan 07 2019 Anton Novojilov <andy@essentialkaos.com> - 1.9.3-0
- Added 2.6.0
- Added 2.6.0-railsexpress
- Added jruby-9.2.1.0
- Added jruby-9.2.2.0
- Added jruby-9.2.3.0
- Added jruby-9.2.4.0
- Added jruby-9.2.4.1
- Added jruby-9.2.5.0
- OpenSSL updated to 1.1.1a for 2.4.0 <-> 2.5.3
- OpenSSL updated to 1.0.2q for 1.9.2-p180 <-> 2.3.8

* Fri Oct 19 2018 Anton Novojilov <andy@essentialkaos.com> - 1.9.2-0
- Added 2.5.3
- Added 2.3.8-railsexpress
- Added 2.4.5-railsexpress
- Added 2.5.3-railsexpress

* Thu Oct 18 2018 Anton Novojilov <andy@essentialkaos.com> - 1.9.1-0
- Added jruby-9.2.0.0
- Added 2.3.8
- Added 2.4.5
- Added 2.5.2
- OpenSSL updated to 1.1.1 for 2.4.0 <-> 2.5.2
- OpenSSL updated to 1.0.2p for 1.9.2-p180 <-> 2.3.8
- Added ruby to dependencies for 2.5.0+

* Fri Apr 27 2018 Anton Novojilov <andy@essentialkaos.com> - 1.9.0-0
- Added jruby-9.1.17.0
- Added EOL dates for 2.2.x and 2.3.x
- Added EOL dates for JRuby 1.6.x and 1.7.x
- Fixed OpenSSL shared lib build
- Added 'no-ssl3' option for OpenSSL

* Thu Mar 29 2018 Gleb Goncharov <g.goncharov@fun-box.ru> - 1.8.1-0
- Added 2.2.10
- Added 2.2.10-railsexpress
- Added 2.3.7
- Added 2.3.7-railsexpress
- Added 2.4.4
- Added 2.4.4-railsexpress
- Added 2.5.1
- Added 2.5.1-railsexpress
- Added jruby-9.1.16.0
- OpenSSL updated to 1.1.0h for 2.4.0 <-> 2.5.0
- OpenSSL updated to 1.0.2o for 1.9.2-p180 <-> 2.3.6

* Fri Feb 02 2018 Anton Novojilov <andy@essentialkaos.com> - 1.8.0-1
- Migrated from kaos.io to kaos.st

* Thu Dec 28 2017 Anton Novojilov <andy@essentialkaos.com> - 1.8.0-0
- Fixed 2.5.0 for build on CentOS6
- Added 2.2.9
- Added 2.2.9-railsexpress
- Added 2.3.6-railsexpress
- Added 2.4.3-railsexpress
- Added 2.5.0-railsexpress

* Tue Dec 26 2017 Anton Novojilov <andy@essentialkaos.com> - 1.7.1-0
- Added 2.3.6
- Added 2.4.3
- Added 2.5.0
- Added jruby-9.1.14.0
- Added jruby-9.1.15.0
- OpenSSL updated to 1.1.0g for 2.4.0-2.5.0
- OpenSSL updated to 1.0.2n for 2.2.8-2.3.6

* Sun Oct 08 2017 Anton Novojilov <andy@essentialkaos.com> - 1.7.0-0
- Added 2.2.8
- Added 2.3.5
- Added 2.4.2
- Added jruby-1.7.27
- Added jruby-9.1.11.0
- Added jruby-9.1.12.0
- Added jruby-9.1.13.0
- Added 2.2.6-railsexpress
- Added 2.2.7-railsexpress
- Added 2.2.8-railsexpress
- Added 2.3.4-railsexpress
- Added 2.3.5-railsexpress
- Added 2.4.1-railsexpress
- Added 2.4.2-railsexpress

* Sun Jun 04 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.6-0
- Added 2.2.7
- Added 2.3.4
- Added jruby-9.1.9.0
- Added jruby-9.1.10.0

* Sat Apr 29 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.5-0
- OpenSSL updated to 1.1.0d for 2.4.0-2.5.0-dev
- OpenSSL updated to 1.0.2k for 1.9.2-2.3.4
- Added 2.3.3-railsexpress
- Added 2.4.0-railsexpress

* Fri Apr 28 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.4-0
- Fixed libyaml linking for 1.9.x

* Thu Mar 30 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.3-0
- Added 2.4.1
- Added jruby-9.1.8.0

* Tue Feb  7 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.2-0
- Added jruby-9.1.7.0

* Fri Dec 30 2016 Anton Novojilov <andy@essentialkaos.com> - 1.6.1-0
- Added 2.4.0
- Removed 2.4.0-preview1, 2.4.0-preview2 and 2.4.0-preview3
- Removed all jruby-9.0.0.0 prerelease versions

* Sun Dec 04 2016 Anton Novojilov <andy@essentialkaos.com> - 1.6.0-1
- Reverted OpenSSL to 1.0.1t for 1.9.1-pXXX

* Sun Nov 27 2016 Anton Novojilov <andy@essentialkaos.com> - 1.6.0-0
- Added jruby-9.1.5.0
- Added jruby-9.1.6.0
- Added 2.2.5
- Added 2.3.2
- Added 2.3.3
- Added 2.4.0-preview2
- Added 2.4.0-preview3
- OpenSSL updated to 1.0.2j

* Fri Sep 02 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.24-0
- Added jruby-9.1.3.0
- Added jruby-9.1.4.0

* Tue Aug 30 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.23-0
- Added jruby-1.7.26

* Fri Jul 22 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.22-0
- Fixed OpenSSL build on i386

* Wed Jul 13 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.21-0
- Added 2.4.0-preview1
- Added jruby-9.1.1.0
- Added jruby-9.1.2.0
- Added 2.0.0-p647-railsexpress
- Added 2.0.0-p648-railsexpress
- Added 2.1.7-railsexpress
- Added 2.1.8-railsexpress
- Added 2.2.3-railsexpress
- Added 2.2.4-railsexpress
- Added 2.2.5-railsexpress
- Added 2.3.0-railsexpress
- Added 2.3.1-railsexpress
- OpenSSL updated to 1.0.1t
- Added EOL dates for 2.1.x

* Thu May 12 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.20-0
- Added 2.3.1
- Added 2.2.5
- Added 2.1.9
- Added 2.1.10
- Added jruby-9.1.0.0

* Thu Apr 28 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.19-0
- Added jruby-1.7.24
- Added jruby-1.7.25

* Tue Mar 01 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.18-0
- OpenSSL updated to 0.9.8w and 1.0.1r
- Added EOL dates for 2.0.0
- Added jruby-9.0.5.0
- Added rubinius-3.16
- Added rubinius-3.17
- Added rubinius-3.18
- Added rubinius-3.19

* Fri Dec 25 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.17-0
- Added 2.3.0

* Thu Dec 17 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.16-0
- Added 2.0.0-p648
- Added 2.1.8
- Added 2.2.4

* Thu Nov 26 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.15-0
- Added jruby-1.7.23

* Fri Nov 20 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.14-0
- Added 2.3.0-preview1

* Thu Nov 19 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.13-0
- Added jruby-9.0.4.0

* Sat Oct 31 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.12-0
- Added jruby-9.0.3.0

* Tue Sep 15 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.11-0
- Added jruby-9.0.1.0
- Added jruby-1.7.22

* Sat Aug 29 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.10-0
- Fixed crc for ruby-1.9.3-p194

* Wed Aug 26 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.9-0
- Fixed crc for jruby-1.7.11

* Tue Aug 25 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.8-0
- Fixed bug with links to latest versions

* Thu Aug 20 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.7-0
- Added 2.0.0-p647
- Added 2.1.7
- Added 2.2.3

* Thu Aug 13 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.6-0
- OpenSSL updated to 1.0.1p

* Sun Aug 09 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.5-0
- Most part links with http changed to https
- Added rubinius-2.5.3
- Added rubinius-2.5.4
- Added rubinius-2.5.5
- Added rubinius-2.5.6
- Added rubinius-2.5.7
- Added rubinius-2.5.8
- Added jruby-9.0.0.0.rc1
- Added jruby-9.0.0.0.rc2
- Added jruby-9.0.0.0
- Added jruby-1.7.21

* Tue May 19 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.4-0
- Added jruby-9.0.0.0.pre2
- Added jruby-1.7.20
- Added 1.9.3-p551-railsexpress
- Added 2.0.0-p594-railsexpress
- Added 2.0.0-p598-railsexpress
- Added 2.0.0-p645-railsexpress
- Added 2.1.4-railsexpress
- Added 2.1.5-railsexpress
- Added 2.1.6-railsexpress
- Added 2.2.0-railsexpress
- Added 2.2.1-railsexpress
- Added 2.2.2-railsexpress
- RubyGems updated to 2.4.7

* Thu Apr 16 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.3-0
- Added 2.0.0-p643
- Added 2.0.0-p645
- Added 2.1.6
- Added 2.2.2
- Added rubinius-2.5.2

* Fri Mar 27 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.2-0
- OpenSSL updated to 1.0.1m and 0.9.8zf

* Tue Mar 03 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.1-0
- Added jruby-1.7.19
- Added 2.2.1

* Wed Jan 21 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.0-0
- All defs updated for compatibility with rbbuild 1.5+

* Wed Dec 10 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.11-0
- Added jruby-1.7.16.2
- Added jruby-1.7.17
- Added rubinius-2.4.0
- Added rubinius-2.4.1

* Fri Nov 21 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.10-0
- Fixed dependencies for rubinius
- Added 1.9.3-p551
- Added 2.0.0-p598
- Added 2.1.5

* Thu Nov 13 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.9-0
- Fixed dependencies for rubinius
- Removed rubinius-2.3.0

* Wed Nov 12 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.8-0
- Added 2.0.0-p594
- Added rubinius-2.3.0

* Thu Oct 30 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.7-0
- Fixed switched rpm/deb dependencies for all rubinius versions

* Wed Oct 29 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.6-0
- Added jruby-1.7.16.1
- Added 2.1.4
- Added 2.1.3-railsexpress
- Fixed bug in 2.1.2-railsexpress

* Sat Oct 18 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.5-0
- OpenSSL updated to 1.0.1j and 0.9.8zc

* Fri Sep 26 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.4-0
- Added jruby-1.7.16

* Sat Sep 20 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.3-0
- Added 2.1.3
- Added 2.0.0-p576
- Added 1.9.2-p330

* Thu Sep 04 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.2-0
- Added jruby-1.7.15

* Tue Sep 02 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.1-0
- Rubygems updated to 2.4.1
- Small fixes

* Mon Sep 01 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.0-0
- New url for essentialkaos mirror
- ca-certificates added to dependencies for all versions which use
  OpenSSL

* Thu Aug 28 2014 Anton Novojilov <andy@essentialkaos.com> - 1.3.2-0
- OpenSSL updated to 1.0.1i
- Added jruby-1.7.14

* Fri Aug 01 2014 Anton Novojilov <andy@essentialkaos.com> - 1.3.1-0
- For all defs used downloaded openssl instead system installed

* Thu Jul 03 2014 Anton Novojilov <andy@essentialkaos.com> - 1.3.0-0
- Maintenance period data added to all def files

* Tue Jul 01 2014 Anton Novojilov <andy@essentialkaos.com> - 1.2.3-0
- OpenSSL updated to 1.0.1h
- Added 2.1.2-railsexpress
- Added 1.9.3-p547 and 1.9.3-p547-railsexpress
- Added 2.0.0-p481 and 2.0.0-p481-railsexpress
- Added jruby-1.7.13
- Added rubinius-2.2.7 rubinius-2.2.8 rubinius-2.2.9 rubinius-2.2.10
- Fixed dependencies in all version of rubinius

* Sat May 10 2014 Anton Novojilov <andy@essentialkaos.com> - 1.2.2-0
- Added 2.1.2
- Updated 2.1.0-railsexpress 2.1.1-railsexpress

* Mon Apr 21 2014 Anton Novojilov <andy@essentialkaos.com> - 1.2.1-0
- Added mruby-1.0.0

* Thu Apr 17 2014 Anton Novojilov <andy@essentialkaos.com> - 1.2.0-0
- Added jruby-1.7.12
- Fixed bug with dependencies in 2.2.0-dev

* Tue Apr 15 2014 Anton Novojilov <andy@essentialkaos.com> - 1.1.6-0
- OpenSSL in all defs updated to 1.0.1g without heartbleed bug

* Sun Apr 06 2014 Anton Novojilov <andy@essentialkaos.com> - 1.1.5-0
- Added rubinius-2.2.6
- Added jruby-1.7.11
- Rubygems updated to 2.2.2
- Libyaml updated to 0.1.6

* Tue Feb 25 2014 Anton Novojilov <andy@essentialkaos.com> - 1.1.4-0
- Added 2.1.1 2.1.1-railsexpress
- Added 2.1.0-railsexpress
- Added 2.0.0-p451 2.0.0-p451-railsexpress
- Added 1.9.3-p545 1.9.3-p545-railsexpress
- Added rubinius-2.2.2 rubinius-2.2.3 rubinius-2.2.4 rubinius-2.2.5
- Dev version updated to 2.2.0
- Added git to dependencies for all railsexpress versions

* Thu Dec 26 2013 Anton Novojilov <andy@essentialkaos.com> - 1.1.3-0
- Added 2.1.0

* Tue Dec 10 2013 Anton Novojilov <andy@essentialkaos.com> - 1.1.2-0
- Added 1.9.3-p484 1.9.3-p484-railsexpress
- Added 2.0.0-p353 2.0.0-p353-railsexpress
- Added rubinius-2.0.0 rubinius-2.1.0 rubinius-2.1.1
- Added rubinius-2.2.0 rubinius-2.2.1
- Removed rubinius-1.2.4

* Sat Aug 24 2013 Anton Novojilov <andy@essentialkaos.com> - 1.1.1-0
- Added --disable-install-doc for most part of rubies

* Wed Aug 21 2013 Anton Novojilov <andy@essentialkaos.com> - 1.1.0-0
- Fixed major bug with install paths

* Tue Jul  2 2013 Anton Novojilov <andy@essentialkaos.com> - 1.0.1-0
- Added 1.9.3-p448-railsexpress

* Tue Jul  2 2013 Anton Novojilov <andy@essentialkaos.com> - 1.0.0-0
- First public release

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
Version:         1.6.0
Release:         1%{?dist}
License:         EKOL
Vendor:          ESSENTIALKAOS
Group:           Development/Tools
URL:             https://github.com/essentialkaos/rbbuild

BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:         %{name}-%{version}.tar.bz2

Requires:        rbbuild

BuildArch:       noarch

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
* Sun Dec 04 2016 Anton Novojilov <andy@essentialkaos.com> - 1.6.0-1
- Reverted OpenSSL to 1.0.1t for 1.9.1-pXXX

* Sun Nov 27 2016 Anton Novojilov <andy@essentialkaos.com> - 1.6.0-0
- Added jruby-9.1.5.0
- Added jruby-9.1.6.0
- Added 2.2.5-p0
- Added 2.3.2-p0
- Added 2.3.3-p0
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
- Added 2.1.7-p0-railsexpress
- Added 2.1.8-p0-railsexpress
- Added 2.2.3-p0-railsexpress
- Added 2.2.4-p0-railsexpress
- Added 2.2.5-p0-railsexpress
- Added 2.3.0-p0-railsexpress
- Added 2.3.1-p0-railsexpress
- OpenSSL updated to 1.0.1t
- Added EOL dates for 2.1.x

* Thu May 12 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.20-0
- Added 2.3.1-p0
- Added 2.2.5-p0
- Added 2.1.9-p0
- Added 2.1.10-p0
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
- Added 2.3.0-p0

* Thu Dec 17 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.16-0
- Added 2.0.0-p648
- Added 2.1.8-p0
- Added 2.2.4-p0

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
- Added 2.1.7-p0
- Added 2.2.3-p0

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
- Added 2.1.4-p0-railsexpress
- Added 2.1.5-p0-railsexpress
- Added 2.1.6-p0-railsexpress
- Added 2.2.0-p0-railsexpress
- Added 2.2.1-p0-railsexpress
- Added 2.2.2-p0-railsexpress
- RubyGems updated to 2.4.7

* Thu Apr 16 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.3-0
- Added 2.0.0-p643
- Added 2.0.0-p645
- Added 2.1.6-p0
- Added 2.2.2-p0
- Added rubinius-2.5.2

* Fri Mar 27 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.2-0
- OpenSSL updated to 1.0.1m and 0.9.8zf

* Tue Mar 03 2015 Anton Novojilov <andy@essentialkaos.com> - 1.5.1-0
- Added jruby-1.7.19
- Added 2.2.1-p0

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
- Added 2.1.5-p0

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
- Added 2.1.4-p0
- Added 2.1.3-p0-railsexpress
- Fixed bug in 2.1.2-p0-railsexpress

* Sat Oct 18 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.5-0
- OpenSSL updated to 1.0.1j and 0.9.8zc

* Fri Sep 26 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.4-0
- Added jruby-1.7.16

* Sat Sep 20 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.3-0
- Added 2.1.3-p0
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
- Added 2.1.2-p0-railsexpress
- Added 1.9.3-p547 and 1.9.3-p547-railsexpress
- Added 2.0.0-p481 and 2.0.0-p481-railsexpress
- Added jruby-1.7.13
- Added rubinius-2.2.7 rubinius-2.2.8 rubinius-2.2.9 rubinius-2.2.10
- Fixed dependencies in all version of rubinius

* Sat May 10 2014 Anton Novojilov <andy@essentialkaos.com> - 1.2.2-0
- Added 2.1.2-p0
- Updated 2.1.0-p0-railsexpress 2.1.1-p0-railsexpress

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
- Added 2.1.1-p0 2.1.1-p0-railsexpress
- Added 2.1.0-p0-railsexpress
- Added 2.0.0-p451 2.0.0-p451-railsexpress
- Added 1.9.3-p545 1.9.3-p545-railsexpress
- Added rubinius-2.2.2 rubinius-2.2.3 rubinius-2.2.4 rubinius-2.2.5
- Dev version updated to 2.2.0
- Added git to dependencies for all railsexpress versions

* Thu Dec 26 2013 Anton Novojilov <andy@essentialkaos.com> - 1.1.3-0
- Added 2.1.0-p0

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

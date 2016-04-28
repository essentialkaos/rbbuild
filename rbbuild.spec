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
Version:         1.5.4
Release:         0%{?dist}
License:         EKOL
Vendor:          ESSENTIALKAOS
Group:           Development/Tools
URL:             http://essentialkaos.com

Source0:         https://source.kaos.io/%{name}/%{name}-%{version}.tar.bz2

Requires:        %{name}-defs
Requires:        gcc make p7zip

BuildArch:       noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
RBBuild provides a simple way to compile and install 
different versions of Ruby on UNIX-like systems.

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
%{_bindir}
%{blds_dir}

################################################################################

%changelog
* Thu Apr 28 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.4-0
- Fixed typo in Mac os name

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
- Fixed bug with depencies check
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

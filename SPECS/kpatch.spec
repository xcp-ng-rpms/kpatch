%global package_speccommit f9952916062838ccf4b0e5c4c00b2c3e5692f6b1
%global usver 0.6.2
%global xsver 5
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit 1696f5db7b5

## kernel_version will be set during build because then kernel-devel
## package installs an RPM macro which sets it. This check keeps
## rpmlint happy.
%if %undefined kernel_version
%define kernel_version dummy
%endif

Name: kpatch
Summary: kernel patch manager
Version: 0.6.2
Release: %{?xsrel}.0.1%{?dist}

License: GPLv2
URL: https://github.com/dynup/kpatch
Source0: kpatch-0.6.2.tar.gz
Patch0: 0001-kpatch-build-Increase-name-length-limit-to-55-chars.patch

Requires: kmod binutils
Requires: kernel-uname-r = %{kernel_version}
BuildRequires: gcc kernel-devel elfutils elfutils-devel
%{?_cov_buildrequires}
Obsoletes: kpatch-modules
Obsoletes: kpatch-4.4.0+10-modules


%description
kpatch is a dynamic kernel patch module manager.  It allows the user to
manage a collection of binary kernel patch modules which can be used to
dynamically patch the kernel without rebooting.


%package devel
Summary: %{name} build tool
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: bc elfutils-libelf-devel

%description devel
The build tool to build live patches for kpatch. The build tool uses the
kernel source and a patch to create a live patch.


%prep
%autosetup -p1
%{?_cov_prepare}
test %{kernel_version} != "dummy"

%build
%{?_cov_wrap} %{__make} PREFIX=/usr KPATCH_BUILD=/lib/modules/%{kernel_version}/build BUILDMOD=no


%install
%{__make} install PREFIX=/usr KPATCH_BUILD=/lib/modules/%{kernel_version}/build DESTDIR=%{buildroot} BUILDMOD=no
rm %{buildroot}/%{_sysconfdir}/init/kpatch.conf
%{?_cov_install}


%files
%{_sbindir}/kpatch
%{_usr}/lib/systemd/system/kpatch.service
%doc %{_mandir}/man1/kpatch.1.gz


%files devel
%{_bindir}/*
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/kpatch-build.1.gz

%{?_cov_results_package}


%changelog
* Thu Nov 14 2024 Yann Dirson <yann.dirson@vates.tech> - 0.6.2-5.0.1
- Bomb out early if kernel_version macro is missing

* Fri Apr 29 2022 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.6.2-5
- Backport a patch from upstream to increase the allowable name length

* Thu Feb 10 2022 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.6.2-4
- CP-38416: Enable static analysis

* Tue Dec 08 2020 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.6.2-3
- CP-35517: Package for koji

* Tue Nov 27 2018 Nathanael Davison <nathanael.davison@citrix.com> - 0.6.2-2
- Removing kernel module part of kpatch.

* Mon Oct 29 2018 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.6.2-1
- Update to v0.6.2.

* Wed Aug 23 2017 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.4.0-1
- Update to the latest commit which is 0.4.0 plus a few bug fixes

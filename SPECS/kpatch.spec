Name: kpatch
Summary: kernel patch manager
Version: 0.6.2
Release: 1%{?dist}

License: GPLv2
URL: https://github.com/dynup/kpatch

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/kpatch/archive?at=1696f5db7b5&format=tar.gz&prefix=kpatch-0.6.2#/kpatch-0.6.2.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/kpatch/archive?at=1696f5db7b5&format=tar.gz&prefix=kpatch-0.6.2#/kpatch-0.6.2.tar.gz) = 1696f5db7b55f53aad6866a266d62650c63b9222


Requires: kmod binutils
Requires: kernel-uname-r = %{kernel_version}
BuildRequires: gcc kernel-devel elfutils elfutils-devel
Obsoletes: kpatch-modules
Obsoletes: kpatch-4.4.0+10-modules


%description
kpatch is a dynamic kernel patch module manager.  It allows the user to
manage a collection of binary kernel patch modules which can be used to
dynamically patch the kernel without rebooting.


%package devel
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/kpatch/archive?at=1696f5db7b5&format=tar.gz&prefix=kpatch-0.6.2#/kpatch-0.6.2.tar.gz) = 1696f5db7b55f53aad6866a266d62650c63b9222
Summary: %{name} build tool
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: bc elfutils-libelf-devel

%description devel
The build tool to build live patches for kpatch. The build tool uses the
kernel source and a patch to create a live patch.


%prep
%autosetup -p1


%build
%{__make} PREFIX=/usr KPATCH_BUILD=/lib/modules/%{kernel_version}/build BUILDMOD=no


%install
%{__make} install PREFIX=/usr KPATCH_BUILD=/lib/modules/%{kernel_version}/build DESTDIR=%{buildroot} BUILDMOD=no
rm %{buildroot}/%{_sysconfdir}/init/kpatch.conf


%files
%{_sbindir}/kpatch
%{_usr}/lib/systemd/system/kpatch.service
%doc %{_mandir}/man1/kpatch.1.gz


%files devel
%{_bindir}/*
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/kpatch-build.1.gz


%changelog
* Tue Nov 27 2018 Nathanael Davison <nathanael.davison@citrix.com> - 0.6.2-2
- Removing kernel module part of kpatch.

* Mon Oct 29 2018 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.6.2-1
- Update to v0.6.2.

* Wed Aug 23 2017 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.4.0-1
- Update to the latest commit which is 0.4.0 plus a few bug fixes

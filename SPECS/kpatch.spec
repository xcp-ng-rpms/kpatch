Name: kpatch
Summary: kernel patch manager
Version: 0.4.0
Release: 1

License: GPLv2
URL: https://github.com/dynup/kpatch
Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/%{name}/archive?at=2ef755bbb96c77ce439a2d8825feadaabc9fe3c9&format=tar.gz&prefix=%{name}-%{version}#/%{name}-%{version}.tar.gz

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
Summary: %{name} build tool
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The build tool to build live patches for kpatch. The build tool uses the
kernel source and a patch to create a live patch.


%prep
%autosetup -p1


%build
%{__make} PREFIX=/usr KPATCH_BUILD=/lib/modules/%{kernel_version}/build


%install
%{__make} install PREFIX=/usr KPATCH_BUILD=/lib/modules/%{kernel_version}/build DESTDIR=%{buildroot}

# mark modules executable so that strip-to-file can strip them
find %{buildroot} -name "*.ko" -type f | xargs chmod u+x


%files
%{_sbindir}/kpatch
%{_usr}/lib/%{name}
%{_usr}/lib/systemd/system/kpatch.service
%doc %{_mandir}/man1/kpatch.1.gz


%files devel
%{_bindir}/*
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/kpatch-build.1.gz


%changelog
* Wed Aug 23 2017 Ross Lagerwall <ross.lagerwall@citrix.com> - 0.4.0-1
- Update to the latest commit which is 0.4.0 plus a few bug fixes

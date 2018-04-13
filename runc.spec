%global with_devel 0
%global with_bundled 1
%global with_check 0

%if 0%{?fedora} || 0%{?rhel} == 6
%global with_debug 1
%global with_unit_test 1
%else
%global with_debug 0
%global with_unit_test 0
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global provider github
%global provider_tld com
%global project opencontainers
%global repo runc
# https://github.com/opencontainers/runc
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path %{provider_prefix}
%global git0 https://github.com/opencontainers/runc
%global commit0 f753f300ae6a725becddbacf15955a0a03b895cb
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: %{repo}
%if 0%{?fedora} || 0%{?rhel} == 6
Epoch: 2
%endif
Version: 1.0.0
Release: 22.git%{shortcommit0}%{?dist}
Summary: CLI for running Open Containers
License: ASL 2.0
URL: %{git0}
Source0: %{git0}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
#ExclusiveArch: %%{?go_arches:%%{go_arches}}%%{!?go_arches:%%{ix86} x86_64 %%{arm}}
ExclusiveArch: %{ix86} x86_64 %{arm} aarch64 ppc64le %{mips} s390x
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires: %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires: pkgconfig(libseccomp)
BuildRequires: go-md2man
%if 0%{?centos}
BuildRequires: make
%endif

%if ! 0%{?with_bundled}
BuildRequires: golang(github.com/Sirupsen/logrus)
BuildRequires: golang(github.com/codegangsta/cli)
BuildRequires: golang(github.com/coreos/go-systemd/activation)
BuildRequires: golang(github.com/coreos/go-systemd/dbus)
BuildRequires: golang(github.com/coreos/go-systemd/util)
BuildRequires: golang(github.com/docker/docker/pkg/mount)
BuildRequires: golang(github.com/docker/docker/pkg/symlink)
BuildRequires: golang(github.com/docker/docker/pkg/term)
BuildRequires: golang(github.com/docker/go-units)
BuildRequires: golang(github.com/godbus/dbus)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/opencontainers/runtime-spec/specs-go)
BuildRequires: golang(github.com/opencontainers/specs/specs-go)
BuildRequires: golang(github.com/seccomp/libseccomp-golang)
BuildRequires: golang(github.com/syndtr/gocapability/capability)
BuildRequires: golang(github.com/vishvananda/netlink)
BuildRequires: golang(github.com/vishvananda/netlink/nl)
%endif
Requires(pre): container-selinux >= 2:2.2-2


%if ! 0%{?centos}
%ifnarch s390x
Recommends: criu
%endif
%else
Requires: criu
%endif

%description
The runc command can be used to start containers which are packaged
in accordance with the Open Container Initiative's specifications,
and to manage containers running under runc.

%if 0%{?with_devel}
%package devel
Summary: %{summary}
BuildArch: noarch

%if 0%{?with_check}
BuildRequires: golang(github.com/Sirupsen/logrus)
BuildRequires: golang(github.com/coreos/go-systemd/dbus)
BuildRequires: golang(github.com/coreos/go-systemd/util)
BuildRequires: golang(github.com/docker/docker/pkg/mount)
BuildRequires: golang(github.com/docker/docker/pkg/symlink)
BuildRequires: golang(github.com/docker/go-units)
BuildRequires: golang(github.com/godbus/dbus)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/opencontainers/runtime-spec/specs-go)
BuildRequires: golang(github.com/seccomp/libseccomp-golang)
BuildRequires: golang(github.com/syndtr/gocapability/capability)
BuildRequires: golang(github.com/vishvananda/netlink)
BuildRequires: golang(github.com/vishvananda/netlink/nl)
%endif

Requires: golang(github.com/Sirupsen/logrus)
Requires: golang(github.com/coreos/go-systemd/dbus)
Requires: golang(github.com/coreos/go-systemd/util)
Requires: golang(github.com/docker/docker/pkg/mount)
Requires: golang(github.com/docker/docker/pkg/symlink)
Requires: golang(github.com/docker/go-units)
Requires: golang(github.com/godbus/dbus)
Requires: golang(github.com/golang/protobuf/proto)
Requires: golang(github.com/opencontainers/runtime-spec/specs-go)
Requires: golang(github.com/seccomp/libseccomp-golang)
Requires: golang(github.com/syndtr/gocapability/capability)
Requires: golang(github.com/vishvananda/netlink)
Requires: golang(github.com/vishvananda/netlink/nl)

Provides: golang(%{import_path}/libcontainer) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/apparmor) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/cgroups) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/cgroups/fs) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/cgroups/systemd) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/configs) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/configs/validate) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/criurpc) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/devices) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/integration) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/keys) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/nsenter) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/seccomp) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/specconv) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/stacktrace) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/system) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/user) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/utils) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/xattr) = %{version}-%{release}

%description devel
The runc command can be used to start containers which are packaged
in accordance with the Open Container Initiative's specifications,
and to manage containers running under runc.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%package unit-test
Summary: Unit tests for %{name} package
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires: %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%if 0%{?with_check}
#Here comes all BuildRequires: PACKAGE the unit tests
#in %%check section need for running
%endif

# test subpackage tests code from devel subpackage
Requires: %{name}-devel = %{epoch}:%{version}-%{release}

%description unit-test
The runc command can be used to start containers which are packaged
in accordance with the Open Container Initiative's specifications,
and to manage containers running under runc.

This package contains unit tests for project
providing packages with %{import_path} prefix.
%endif

%prep
%setup -q -n %{name}-%{commit0}

%build
mkdir -p GOPATH
pushd GOPATH
    mkdir -p src/%{provider}.%{provider_tld}/%{project}
    ln -s $(dirs +1 -l) src/%{import_path}
popd

pushd GOPATH/src/%{import_path}
export GOPATH=%{gopath}:$(pwd)/GOPATH

make BUILDTAGS="seccomp selinux" all

sed -i '/\#\!\/bin\/bash/d' contrib/completions/bash/%{name}

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}

# generate man pages
man/md2man-all.sh

# install man pages
install -d -p %{buildroot}%{_mandir}/man8
install -p -m 0644 man/man8/*.8 %{buildroot}%{_mandir}/man8/.
# install bash completion
install -d -p %{buildroot}%{_datadir}/bash-completion/completions
install -p -m 0644 contrib/completions/bash/%{name} %{buildroot}%{_datadir}/bash-completion/completions

# source codes for building projects
%if 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *.go but no *_test.go files and generate devel.file-list
for file in $(find . -iname "*.go" \! -iname "*_test.go" | grep -v "^./Godeps") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
for file in $(find . -iname "*.proto" | grep -v "^./Godeps") ; do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
done
%endif

# testing files for this project
%if 0%{?with_unit_test} && 0%{?with_devel}
install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
# find all *_test.go files and generate unit-test.file-list
for file in $(find . -iname "*_test.go" | grep -v "^./Godeps"); do
    echo "%%dir %%{gopath}/src/%%{import_path}/$(dirname $file)" >> devel.file-list
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$(dirname $file)
    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test.file-list
done
%endif

%if 0%{?with_devel}
sort -u -o devel.file-list devel.file-list
%endif

%check
%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
%if ! 0%{?with_bundled}
export GOPATH=%{buildroot}/%{gopath}:%{gopath}
%else
export GOPATH=%{buildroot}/%{gopath}:$(pwd)/Godeps/_workspace:%{gopath}
%endif

%if ! 0%{?gotest:1}
%global gotest go test
%endif

# FAIL: TestFactoryNewTmpfs (0.00s), factory_linux_test.go:59: operation not permitted
#%%gotest %%{import_path}/libcontainer
#%%gotest %%{import_path}/libcontainer/cgroups
# --- FAIL: TestInvalidCgroupPath (0.00s)
#       apply_raw_test.go:16: couldn't get cgroup root: mountpoint for cgroup not found
#       apply_raw_test.go:25: couldn't get cgroup data: mountpoint for cgroup not found
#%%gotest %%{import_path}/libcontainer/cgroups/fs
#%%gotest %%{import_path}/libcontainer/configs
#%%gotest %%{import_path}/libcontainer/devices
# undefined reference to `nsexec'
#%%gotest %%{import_path}/libcontainer/integration
# Unable to create tstEth link: operation not permitted
#%%gotest %%{import_path}/libcontainer/netlink
# undefined reference to `nsexec'
#%%gotest %%{import_path}/libcontainer/nsenter
#%%gotest %%{import_path}/libcontainer/stacktrace
#constant 2147483648 overflows int
#%%gotest %%{import_path}/libcontainer/user
#%%gotest %%{import_path}/libcontainer/utils
#%%gotest %%{import_path}/libcontainer/xattr
%endif

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc MAINTAINERS_GUIDE.md PRINCIPLES.md README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_mandir}/man8/%{name}*
%{_datadir}/bash-completion/completions/%{name}

%if 0%{?with_devel}
%files devel -f devel.file-list
%license LICENSE
%doc MAINTAINERS_GUIDE.md PRINCIPLES.md README.md CONTRIBUTING.md
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%dir %{gopath}/src/%{import_path}
%endif

%if 0%{?with_unit_test} && 0%{?with_devel}
%files unit-test -f unit-test.file-list
%license LICENSE
%doc MAINTAINERS_GUIDE.md PRINCIPLES.md README.md CONTRIBUTING.md
%endif

%changelog
* Fri Apr 13 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:1.0.0-22.gitf753f30
- Resolves: #1567229
- built commit f753f30

* Mon Apr 09 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:1.0.0-21.gitcc4307a
- autobuilt commit cc4307a

* Mon Mar 12 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2:1.0.0-20.rc5.git4bb1fe4
- Rebuild for aarch64 install issue

* Tue Feb 27 2018 Dan Walsh <dwalsh@redhat.name> - 2:1.0.0-19.rc5.git4bb1fe4
- release v1.0.0~rc5

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.0.0-17.rc4.git9f9c962.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Dan Walsh <dwalsh@redhat.name> - 2:1.0.0-17.rc4.git9f9c962
- Bump to the latest from upstream

* Tue Dec 26 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:1.0.0-16.rc4.gite6516b3
- install bash completion to correct location
- remove shebang from bash completion gh#1679
- correct rpmlint issues

* Mon Dec 18 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:1.0.0-15.rc4.gite6516b3
- built commit e6516b3

* Fri Dec 15 2017 Dan Walsh <dwalsh@redhat.name> - 2:1.0.0-14.rc4.gitdb093f6
- Lots of fixes for libcontainer
- support unbindable,runbindable for rootfs propagation

* Sun Dec 10 2017 Dan Walsh <dwalsh@redhat.name> - 2:1.0.0-13.rc4.git1d3ab6d
- Many Stability fixes
- Many fixes for rootless containers
- Many fixes for static builds

* Wed Oct 25 2017 Dan Walsh <dwalsh@redhat.name> - 2:1.0.0-12.rc4.gitaea4f21
- Add container-selinux prerequires to make sure runc is labeled correctly

* Tue Sep 12 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:1.0.0-11.rc4.gitaea4f21
- disable devel package and %%check - makes life easier for module building

* Tue Sep 5 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:1.0.0-10.rc4.gitaea4f21
- bump Epoch to 2 since bump to v1.0.1 was in error
- bump to v1.0.0-rc4
- built commit aea4f21

* Tue Sep 5 2017 Dan Walsh <dwalsh@redhat.name> - 1.0.1-4.rc.gitaea4f21
- Rebuilt from master, with requierements needed for CRI-O

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.1-3.gitc5ec254
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.1-2.gitc5ec254
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Dan Walsh <dwalsh@redhat.name> - 1.0.1-1.gitc5ec25487
- v1.0.0-rc5 release of runc

* Tue Jun 27 2017 Till Maas <opensource@till.name> - 1.0.0-9.git6394544
- Just make the criu dependency optional (https://bugzilla.redhat.com/show_bug.cgi?id=1460148)

* Tue Jun 27 2017 Till Maas <opensource@till.name> - 1.0.0-8.git6394544.1
- Do not build for ix86: there is no criu on ix86

* Fri Jun 02 2017 Antonio Murdaca <runcom@fedoraproject.org> - 1:1.0.0-7.git6394544.1
- rebuilt

* Fri Mar 24 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1:1.0.0-6.git75f8da7
- bump to v1.0.0-rc3
- built opencontainers/v1.0.0-rc3 commit 75f8da7

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.0-5.rc2.gitc91b5be.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 01 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1:1.0.0-5.rc2
- depend on criu for checkpoint/restore

* Wed Jan 18 2017 Dennis Gilmore <dennis@ausil.us> - 1:1.0.0-4.rc2
- enable aarch64

* Wed Jan 11 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1:1.0.0-3.rc2
- Resolves: #1412238 - *CVE-2016-9962* - set init processes as non-dumpable,
runc patch from Michael Crosby <crosbymichael@gmail.com>

* Fri Jan 06 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1:1.0.0-2.rc2.git47ea5c7
- patch to enable seccomp
- Pass $BUILDTAGS to the compiler in cases where we don't have to define
gobuild for ourselves.
- From: Nalin Dahyabhai <nalin@redhat.com>

* Wed Dec 21 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1:1.0.0-1.rc2.git47ea5c7
- bump to 1.0.0 rc2
- built commit 47ea5c7
- build with bundled sources for now (some new dependencies need to be packaged)

* Wed Aug 24 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1:1.0.0-1.rc1.git04f275d
- Resolves: #1342707 - bump to v1.0.0-rc1
- built commit 04f275d
- cosmetic changes to make rpmlint happy

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.1.1-4.git57b9972
- https://fedoraproject.org/wiki/Changes/golang1.7

* Thu May 26 2016 jchaloup <jchaloup@redhat.com> - 1:0.1.1-3.git57b9972
- Add bash completion
  resolves: #1340119

* Thu May 19 2016 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1:0.1.1-2.gitbaf6536
- add selinux to BUILDTAGS in addition to the default seccomp tag

* Tue Apr 26 2016 jchaloup <jchaloup@redhat.com> - 1:0.1.1-0.1.gitbaf6536
- Update to v0.1.1
  resolves: #1330378

* Tue Apr 12 2016 jchaloup <jchaloup@redhat.com> - 1:0.0.9-0.3.git94dc520
- Ship man pages too
  resolves: #1326115

* Wed Apr 06 2016 jchaloup <jchaloup@redhat.com> - 1:0.0.9-0.2.git94dc520
- Extend supported architectures to golang_arches
  Disable failing test
  related: #1290943

* Wed Mar 16 2016 jchaloup <jchaloup@redhat.com> - 1:0.0.9-0.1.git94dc520
- Update to 0.0.9
  resolves: #1290943

* Wed Mar 02 2016 jchaloup <jchaloup@redhat.com> - 1:0.0.8-0.1.git1a124e9
- Update to 0.0.8

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.0.5-0.4.git97bc9a7
- https://fedoraproject.org/wiki/Changes/golang1.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.5-0.3.git97bc9a7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 jchaloup <jchaloup@redhat.com> - 1:0.0.5-0.2.git97bc9a7
- unit-test-devel subpackage requires devel with correct epoch

* Wed Nov 25 2015 jchaloup <jchaloup@redhat.com> - 1:0.0.5-0.1.git97bc9a7
- Update to 0.0.5, introduce Epoch for Fedora due to 0.2 version instead of 0.0.2
  resolves: #1286114

* Fri Aug 21 2015 Jan Chaloupka <jchaloup@redhat.com> - 0.2-0.2.git90e6d37
- First package for Fedora
  resolves: #1255179

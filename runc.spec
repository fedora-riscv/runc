%if 0%{?fedora} || 0%{?rhel} == 6
%global with_devel 1
# TODO: package new deps
%global with_bundled 1
%global with_debug 1
%global with_check 1
%global with_unit_test 1
%else
%global with_devel 0
%global with_bundled 1
%global with_debug 0
%global with_check 0
%global with_unit_test 0
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global	debug_package	%{nil}
%endif

%global	provider github
%global	provider_tld com
%global project opencontainers
%global repo runc
# https://github.com/opencontainers/runc
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path %{provider_prefix}
%global commit 47ea5c75ebeb40a317d2cfa95f9c3536c00c1eea
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: %{repo}
%if 0%{?fedora} || 0%{?rhel} == 6
Epoch: 1
%endif
Version: 1.0.0
Release: 2.rc2.git%{shortcommit}%{?dist}
Summary: CLI for running Open Containers
License: ASL 2.0
URL: https://%{provider_prefix}
Source0: https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
#ExclusiveArch: %%{?go_arches:%%{go_arches}}%%{!?go_arches:%%{ix86} x86_64 %{arm}}
ExclusiveArch: %{ix86} x86_64 %{arm} ppc64le %{mips} s390x
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires: %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

BuildRequires: pkgconfig(libseccomp)
BuildRequires: go-md2man

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
Provides: golang(%{import_path}/libcontainer/label) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/nsenter) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/seccomp) = %{version}-%{release}
Provides: golang(%{import_path}/libcontainer/selinux) = %{version}-%{release}
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
%setup -q -n %{repo}-%{commit}

%build
mkdir -p src/github.com/opencontainers
ln -s ../../../ src/github.com/opencontainers/runc

%if ! 0%{?with_bundled}
export GOPATH=$(pwd):%{gopath}
%else
export GOPATH=$(pwd):$(pwd)/Godeps/_workspace:%{gopath}
%endif

BUILDTAGS="seccomp selinux"
%if ! 0%{?gobuild:1}
%define gobuild() go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{**};

%endif

%gobuild -tags "$BUILDTAGS" -o bin/%{name} %{import_path}

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 755 bin/%{name} %{buildroot}%{_bindir}

# generate man pages
man/md2man-all.sh

# install man pages
install -d -p %{buildroot}%{_mandir}/man8
install -p -m 0644 man/man8/*.8 %{buildroot}%{_mandir}/man8/.
# install bash completion
install -d -p %{buildroot}%{_sysconfdir}/bash_completion.d/
install -p -m 0644 contrib/completions/bash/runc %{buildroot}%{_sysconfdir}/bash_completion.d/.

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
%gotest %{import_path}/libcontainer/cgroups
# --- FAIL: TestInvalidCgroupPath (0.00s)
#	apply_raw_test.go:16: couldn't get cgroup root: mountpoint for cgroup not found
#	apply_raw_test.go:25: couldn't get cgroup data: mountpoint for cgroup not found
#%%gotest %%{import_path}/libcontainer/cgroups/fs
%gotest %{import_path}/libcontainer/configs
%gotest %{import_path}/libcontainer/devices
# undefined reference to `nsexec'
#%%gotest %%{import_path}/libcontainer/integration
%gotest %{import_path}/libcontainer/label
# Unable to create tstEth link: operation not permitted
#%%gotest %%{import_path}/libcontainer/netlink
# undefined reference to `nsexec'
#%%gotest %%{import_path}/libcontainer/nsenter
%gotest %{import_path}/libcontainer/selinux
%gotest %{import_path}/libcontainer/stacktrace
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
%{_mandir}/man8/.
%{_sysconfdir}/bash_completion.d/runc

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
* Fri Jan 06 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 1:1.0.0-2.rc2.git47ea5c7
- patch to enable seccomp
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

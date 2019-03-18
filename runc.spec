%global with_devel 0
%global with_bundled 1
%global with_check 0
%global with_unit_test 0
%global with_debug 1

%if 0%{?with_debug}
%global _find_debuginfo_dwz_opts %{nil}
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
%global commit0 f56b4cbeadc407e715d9b2ba49e62185bd81cef4
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: %{repo}
Epoch: 2
Version: 1.0.0
Release: 83.dev.git%{shortcommit0}%{?dist}
Summary: CLI for running Open Containers
License: ASL 2.0
URL: %{git0}
Source0: %{git0}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0: 1807.patch

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
#ExclusiveArch: %%{?go_arches:%%{go_arches}}%%{!?go_arches:%%{ix86} x86_64 %%{arm}}
ExclusiveArch: %{ix86} x86_64 %{arm} aarch64 ppc64le %{mips} s390x
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires: %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires: pkgconfig(libseccomp)
BuildRequires: go-md2man
BuildRequires: make
BuildRequires: git

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
Recommends: container-selinux >= 2:2.2-2

%ifnarch s390x
Recommends: criu
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
%autosetup -Sgit -n %{name}-%{commit0}

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
* Mon Mar 18 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:1.0.0-83.dev.gitf56b4cb
- release tag higher than f29 to ensure smooth upgrade
- container-selinux is a recommends and not a requires

* Mon Mar 18 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:1.0.0-76.dev.gitf56b4cb
- built f56b4cb

* Sat Feb 16 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-75.dev.git751f18d
- autobuilt 751f18d

* Thu Feb 14 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-74.dev.gitf414f49
- autobuilt f414f49

* Wed Feb 13 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-73.dev.git0a012df
- autobuilt 0a012df

* Tue Feb 12 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-72.dev.git6635b4f
- autobuilt 6635b4f

* Sat Feb 09 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-71.dev.gitdd023c4
- autobuilt dd023c4

* Sat Feb 02 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-70.dev.gite4fa8a4
- autobuilt e4fa8a4

* Sat Jan 26 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-69.dev.git8011af4
- autobuilt 8011af4

* Wed Jan 16 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-68.dev.gitc1e454b
- autobuilt c1e454b

* Tue Jan 15 2019 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-67.dev.git12f6a99
- autobuilt 12f6a99

* Fri Dec 21 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-66.dev.gitbbb17ef
- autobuilt bbb17ef

* Tue Dec 11 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-65.dev.gitf5b9991
- autobuilt f5b9991

* Sun Dec 09 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-64.dev.git859f745
- autobuilt 859f745

* Wed Dec 05 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-63.dev.git25f3f89
- autobuilt 25f3f89

* Tue Dec 04 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-62.dev.git96ec217
- autobuilt 96ec217

* Tue Nov 27 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-61.dev.git4932620
- autobuilt 4932620

* Sun Nov 25 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-60.dev.git9397a6f
- autobuilt 9397a6f

* Sat Nov 24 2018 Dan Walsh <dwalsh@redhat.name> - 2:1.0.0-59.dev.gitccb5efd3
- rc6 build

* Wed Nov 07 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-58.dev.git079817c
- autobuilt 079817c

* Thu Nov 01 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:1.0.0-57.dev.git9e5aa74
- built commit 9e5aa74

* Tue Oct 16 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:1.0.0-56.dev.git78ef28e
- built commit 78ef28e
 
* Tue Sep 25 2018 Dan Walsh <dwalsh@redhat.name> - 2:1.0.0-55.dev.gitfdd8055
- built commit 578fe65e4fb86b95cc67b304d99d799f976dc40c

* Mon Sep 24 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:1.0.0-54.dev.git00dc700
- built commit 00dc700
- rebase 1807.patch
- enable debuginfo for all versions

* Fri Sep 07 2018 baude <bbaude@redhat.com> - 2:1.0.0-53.dev.git70ca035
- Add BuildRequires git

* Thu Sep 06 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:1.0.0-52.dev.git70ca035
- built commit 70ca035

* Fri Aug 31 2018 Dan Walsh <dwalsh@redhat.name> - 2:1.0.0-51.dev.gitfdd8055
- Fix handling of tmpcopyup

* Wed Aug 15 2018 Dan Walsh <dwalsh@redhat.name> - 2:1.0.0-50.dev.git20aff4f
- Revert minor cleanup patch

* Tue Aug 7 2018 Dan Walsh <dwalsh@redhat.name> - 2:1.0.0-49.dev.gitb4056a4
- Pass GOMAXPROCS to init processes

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2:1.0.0-48.dev.gitbeadf0e
- Rebuild with fixed binutils

* Sun Jul 29 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-47.dev.gitbeadf0e
- autobuilt beadf0e

* Fri Jul 27 2018 Dan Walsh <dwalsh@redhat.name> - 2:1.0.0-46.dev.gitb4e2ecb
- Add patch https://github.com/opencontainers/runc/pull/1807 to allow
- runc and podman to work with sd_notify

* Thu Jul 26 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-45.dev.gitb4e2ecb
- autobuilt b4e2ecb

* Wed Jul 25 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-44.dev.gitbc14672
- autobuilt bc14672

* Fri Jul 20 2018 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:1.0.0-43.dev.git21ac086
- Resolves: #1606281 - temp disable debuginfo for rawhide

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:1.0.0-42.dev.git21ac086
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-41.dev.git21ac086
- autobuilt 21ac086

* Fri Jul 06 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-40.git45e08f6
- autobuilt 45e08f6

* Tue Jun 26 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-39.git2c632d1
- autobuilt 2c632d1

* Mon Jun 25 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-38.git3ccfa2f
- autobuilt 3ccfa2f

* Sun Jun 24 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-37.git0154d05
- autobuilt 0154d05

* Sat Jun 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-36.gitad0f525
- autobuilt ad0f525

* Tue Jun 05 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-35.gitdd56ece
- autobuilt dd56ece

* Sun Jun 03 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-34.git2e91544
- autobuilt 2e91544

* Thu May 31 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-33.gitecd55a4
- autobuilt ecd55a4

* Fri May 25 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-32.gitdd67ab1
- autobuilt dd67ab1

* Fri Apr 27 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-31.git0cbfd83
- autobuilt commit 0cbfd83

* Tue Apr 24 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-30.git871ba2e
- autobuilt commit 871ba2e

* Fri Apr 20 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-29.git1f11dc5
- autobuilt commit 1f11dc5

* Thu Apr 19 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-28.git63e6708
- autobuilt commit 63e6708

* Tue Apr 17 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-27.gitd56f6cc
- autobuilt commit d56f6cc

* Tue Apr 17 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-26.gitd56f6cc
- autobuilt commit d56f6cc

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-25.gitd56f6cc
- autobuilt commit d56f6cc

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-24.gitd56f6cc
- autobuilt commit d56f6cc

* Mon Apr 16 2018 Lokesh Mandvekar (Bot) <lsm5+bot@fedoraproject.org> - 2:1.0.0-23.gitf753f30
- autobuilt commit f753f30

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

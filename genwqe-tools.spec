Summary:             GenWQE userspace tools
Name:                genwqe-tools
Version:             4.0.20
Release:             1
License:             ASL 2.0
URL:                 https://github.com/ibm-genwqe/genwqe-user/
BuildRequires:       gcc zlib-devel >= 1.2.7 help2man
%ifarch %{power64}
BuildRequires:       libcxl-devel
%endif
Source0:             https://github.com/ibm-genwqe/genwqe-user/archive/v%{version}.tar.gz#/genwqe-user-%{version}.tar.gz
Patch0:              genwqe-user-4.0.18-install-gzFile_test.patch
Patch1:              genwqe-user-4.0.18-modifyFuntionName.patch
Requires:            genwqe-zlib = %{version}-%{release}
%description
Provide a suite of utilities to manage and configure the IBM GenWQE card.

%package -n genwqe-zlib
Summary:             GenWQE hardware accelerated libz
%description -n genwqe-zlib
GenWQE hardware accelerated libz and test-utilities.

%package -n genwqe-vpd
Summary:             GenWQE adapter VPD tools
%description -n genwqe-vpd
The genwqe-vpd package contains GenWQE adapter VPD tools.

%package -n genwqe-zlib-devel
Summary:             Development files for %{name}
Requires:            genwqe-zlib%{?_isa} = %{version}-%{release}
%description -n genwqe-zlib-devel
The genwqe-zlib-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n genwqe-zlib-static
Summary:             Static library files for %{name}
Requires:            genwqe-zlib-devel%{?_isa} = %{version}-%{release}
%description -n genwqe-zlib-static
The genwqe-zlib-static package contains static libraries for
developing applications that use %{name}.

%prep
%autosetup -p1 -n genwqe-user-%{version}

%build
LDFLAGS="%{__global_ldflags}" CFLAGS="%{optflags}" make %{?_smp_mflags} tools lib \
 VERSION=%{version} CONFIG_ZLIB_PATH=%{_libdir}/libz.so V=2

%install
make %{?_smp_mflags} install DESTDIR=%{buildroot}/%{_prefix} \
    SYSTEMD_UNIT_DIR=%{buildroot}/%{_unitdir} \
    LIB_INSTALL_PATH=%{buildroot}/%{_libdir}/genwqe \
    INCLUDE_INSTALL_PATH=%{buildroot}/%{_includedir}/genwqe
mkdir -p %{buildroot}/%{_sysconfdir}/
install -m 0644 tools/genwqe_vpd.csv %{buildroot}/etc/
rm %{buildroot}%{_libdir}/genwqe/libz.*
mv %{buildroot}%{_libdir}/genwqe/* %{buildroot}%{_libdir}/
rmdir %{buildroot}%{_libdir}/genwqe/
%ldconfig_scriptlets -n genwqe-zlib

%files -n genwqe-tools
%license LICENSE
%{_bindir}/genwqe_echo
%{_bindir}/genwqe_ffdc
%{_bindir}/genwqe_cksum
%{_bindir}/genwqe_memcopy
%{_bindir}/genwqe_peek
%{_bindir}/genwqe_poke
%{_bindir}/genwqe_update
%{_bindir}/genwqe_gunzip
%{_bindir}/genwqe_gzip
%{_bindir}/genwqe_test_gz
%{_bindir}/genwqe_mt_perf
%{_bindir}/zlib_mt_perf
%{_bindir}/gzFile_test
%{_mandir}/man1/genwqe_echo.1*
%{_mandir}/man1/genwqe_ffdc.1*
%{_mandir}/man1/genwqe_gunzip.1*
%{_mandir}/man1/genwqe_gzip.1*
%{_mandir}/man1/genwqe_cksum.1*
%{_mandir}/man1/genwqe_memcopy.1*
%{_mandir}/man1/genwqe_peek.1*
%{_mandir}/man1/genwqe_poke.1*
%{_mandir}/man1/genwqe_update.1*
%{_mandir}/man1/zlib_mt_perf.1*
%{_mandir}/man1/genwqe_test_gz.1*
%{_mandir}/man1/genwqe_mt_perf.1*
%{_mandir}/man1/gzFile_test.1*
%ifarch %{power64}
%{_bindir}/genwqe_maint
%{_bindir}/genwqe_loadtree
/%{_unitdir}/genwqe_maint.service
%{_mandir}/man1/genwqe_maint.1*
%{_mandir}/man1/genwqe_loadtree.1*
%endif

%files -n genwqe-zlib
%license LICENSE
%{_libdir}/*.so.*

%files -n genwqe-vpd
%license LICENSE
%config(noreplace) %{_sysconfdir}/genwqe_vpd.csv
%{_bindir}/genwqe_csv2vpd
%{_bindir}/genwqe_vpdconv
%{_bindir}/genwqe_vpdupdate
%{_mandir}/man1/genwqe_csv2vpd.1*
%{_mandir}/man1/genwqe_vpdconv.1*
%{_mandir}/man1/genwqe_vpdupdate.1*

%files -n genwqe-zlib-devel
%dir %{_includedir}/genwqe
%{_includedir}/genwqe/*
%{_libdir}/*.so

%files -n genwqe-zlib-static
%{_libdir}/*.a

%changelog
* Thu Aug 13 2020 tuShenmei <tushenmei@huawei.com> - 4.0.20-1
- package init

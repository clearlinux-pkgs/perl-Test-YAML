#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-YAML
Version  : 1.07
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/T/TI/TINITA/Test-YAML-1.07.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TI/TINITA/Test-YAML-1.07.tar.gz
Summary  : Testing Module for YAML Implementations
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-YAML-bin = %{version}-%{release}
Requires: perl-Test-YAML-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Spiffy)
BuildRequires : perl(Test::Base)

%description
NAME
Test::YAML - Testing Module for YAML Implementations
VERSION
This document describes Test::YAML version 1.07.

%package bin
Summary: bin components for the perl-Test-YAML package.
Group: Binaries
Requires: perl-Test-YAML-license = %{version}-%{release}

%description bin
bin components for the perl-Test-YAML package.


%package dev
Summary: dev components for the perl-Test-YAML package.
Group: Development
Requires: perl-Test-YAML-bin = %{version}-%{release}
Provides: perl-Test-YAML-devel = %{version}-%{release}
Requires: perl-Test-YAML = %{version}-%{release}

%description dev
dev components for the perl-Test-YAML package.


%package license
Summary: license components for the perl-Test-YAML package.
Group: Default

%description license
license components for the perl-Test-YAML package.


%prep
%setup -q -n Test-YAML-1.07

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-YAML
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-YAML/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Test/YAML.pm
/usr/lib/perl5/vendor_perl/5.28.2/Test/YAML.pod

%files bin
%defattr(-,root,root,-)
/usr/bin/test-yaml

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::YAML.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-YAML/LICENSE

%{?scl:%scl_package perl-Authen-PAM}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global baserelease 3

Name:           %{?scl_prefix}perl-Authen-PAM
Version:        0.16
Release:        25.%{baserelease}%{?dist}
Summary:        Authen::PAM Perl module
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Authen-PAM/
Source0:        http://www.cpan.org/authors/id/N/NI/NIKIP/Authen-PAM-%{version}.tar.gz
# Build
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pam-devel
BuildRequires:  perl
BuildRequires:  perl-devel
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
# Runtime
# -
# Tests only
%{?_with_check:BuildRequires:  perl(POSIX)}
%{?_with_check:BuildRequires:  perl(strict)}
%{?_with_check:BuildRequires:  perl(vars)}
Requires:       perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))
Requires:       %{?scl_prefix}runtime

%description
This module provides a Perl interface to the PAM library.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%setup -q -n Authen-PAM-%{version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
make pure_install DESTDIR=%{buildroot}%{?_scl_root}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

# Tests are interactive.
%{?scl:EOF}


%check
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%{?_with_check:make test}
%{?scl:EOF}


%files
%doc Changes README
%{?_scl_root}%{perl_vendorarch}/auto/*
%{?_scl_root}%{perl_vendorarch}/Authen
%{_mandir}/man3/*

%changelog
* Mon Aug 01 2016 Mat Booth <mat.booth@redhat.com> - 0.16-25.3
- Ensure SCL runtime package is installed

* Thu Jul 28 2016 Mat Booth <mat.booth@redhat.com> - 0.16-25.2
- Minor SCL-isation fixes

* Thu Jul 28 2016 Mat Booth <mat.booth@redhat.com> - 0.16-25.1
- Auto SCL-ise package for rh-eclipse46 collection

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.16-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Petr Šabata <contyk@redhat.com> - 0.16-24
- Package cleanup

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-22
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.16-21
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.16-17
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.16-14
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.16-12
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-10
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.16-9
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.16-8
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.16-5
Rebuild for new perl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.16-4
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.16-3
- Rebuild for selinux ppc32 issue.

* Wed Jul 25 2007 Jeremy Katz <katzj@redhat.com> - 0.16-2
- rebuild for toolchain bug

* Mon Jul 16 2007 Steven Pritchard <steve@kspei.com> 0.16-1
- Update to 0.16.
- Canonicalize Source0 URL.
- Fix find option order.
- Use fixperms macro instead of our own chmod incantation.
- Drop our copies of the license files.
- BR ExtUtils::MakeMaker.
- Drop LD_RUN_PATH filter.

* Sat Sep 03 2005 Steven Pritchard <steve@kspei.com> 0.15-2
- Remove explicit core module dependencies.
- Include COPYING and Artistic.
- Misc. minor cleanup.

* Thu Aug 25 2005 Steven Pritchard <steve@kspei.com> 0.15-1
- Specfile autogenerated.

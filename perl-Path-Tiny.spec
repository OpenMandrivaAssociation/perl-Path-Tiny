%define modname	Path-Tiny

Summary:	Perl file path utility
Name:		perl-%{modname}
Version:	0.146
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(open)
BuildRequires:	perl-devel

%description
Perl file path utility

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make_build test

%install
%make_install

%files
%doc README
%{perl_vendorlib}/Path/*
%{_mandir}/man3/*

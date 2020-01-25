#
# Conditional build:
%bcond_without	tests		# perform "make test"
#
%define	pdir	Astro
%define	pnam	satpass
Summary:	Astro-satpass - Perl classes needed to predict satellite visibility
Summary(pl.UTF-8):	Astro-satpass - zbiór klas Perla do przewidywania widzialności satelitów
Name:		perl-Astro-satpass
Version:	0.111
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	060b079235c881efa6e457174da01641
URL:		http://search.cpan.org/dist/Astro-satpass/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains classes needed to predict satellite visibility,
and a demonstration application (satpass) that makes use of these
classes. The classes themselves are:

Astro::Coord::ECI - superclass (coordinate transforms)
Astro::Coord::ECI::Moon - Predict location of the Moon.
Astro::Coord::ECI::Star - Predict location of a star.
Astro::Coord::ECI::Sun - Predict location of the Sun.
Astro::Coord::ECI::TLE - Predict location of a satellite.
Astro::Coord::ECI::TLE::Iridium - Subclass of TLE, with the ability
    to predict flares.
Astro::Coord::ECI::TLE::Set - Aggregation of TLEs, with ability
    to use the correct TLE depending on time.
Astro::Coord::ECI::Utils - Constants and utility subroutines.

%description -l pl.UTF-8
Ten pakiet zawiera klasy potrzebne do przewidywania widzialności
satelitów oraz program demonstracyjny (satpass) pokazujący użycie
tych klas. Wspomniane klasy to:

Astro::Coord::ECI - klasa bazowa (transformacja współrzędnych).
Astro::Coord::ECI::Moon - wyznaczanie położenia Księżyca.
Astro::Coord::ECI::Star - wyznaczanie położenia gwiazd.
Astro::Coord::ECI::Sun - wyznaczanie położenia Słońca.
Astro::Coord::ECI::TLE - wyznaczanie położenia satelit.
Astro::Coord::ECI::TLE::Iridium - podklasa TLE, do wyznaczania
    odbłysków (flar) satelit Iridium.
Astro::Coord::ECI::TLE::Set - zbiór klas TLE.
Astro::Coord::ECI::Utils - stałe oraz funkcje pomocznicze.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mkdir} -p $RPM_BUILD_ROOT/%{_bindir}
%{__install} script/satpass $RPM_BUILD_ROOT/%{_bindir}

%{__sed} -i -e 's|#!/usr/local/bin/perl|#!/usr/bin/perl|' $RPM_BUILD_ROOT/%{_bindir}/satpass

%{__mkdir} -p $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__cp} -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} \
	$RPM_BUILD_ROOT%{perl_vendorarch}/auto/Astro/Coord/ECI/.packlist \
	$RPM_BUILD_ROOT%{perl_vendorlib}/Astro/Coord/ECI/OVERVIEW.pod \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/tle_period.t

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/satpass
%{perl_vendorlib}/Astro/Coord/ECI.pm
%{perl_vendorlib}/Astro/Coord/ECI
%{_mandir}/man3/Astro::Coord::ECI*
%{_examplesdir}/%{name}-%{version}

Summary:	fonttosfnt application - wrap a bitmap font in a sfnt (TrueType or OpenType) wrapper
Summary(pl.UTF-8):	Aplikacja fonttosfnt - osadzanie fontu bitmapowego w obudowie sfnt (TrueType lub OpenType)
Name:		xorg-app-fonttosfnt
Version:	1.1.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/fonttosfnt-%{version}.tar.bz2
# Source0-md5:	bf8086aa878f0d1bb7715e5865183cc4
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fonttosfnt application wraps a bitmap (bdf or pcf) font or a set of
bitmap fonts in a sfnt (TrueType or OpenType) wrapper.

%description -l pl.UTF-8
Aplikacja fonttosfnt osadza font bitmapowy (bdf lub pcf) lub zbiór
fontów bitmapowych w obudowie sfnt (TrueType lub OpenType).

%prep
%setup -q -n fonttosfnt-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/fonttosfnt
%{_mandir}/man1/fonttosfnt.1*

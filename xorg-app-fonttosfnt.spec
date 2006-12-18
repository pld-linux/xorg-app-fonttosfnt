Summary:	fonttosfnt application - wrap a bitmap font in a sfnt (TrueType) wrapper
Summary(pl):	Aplikacja fonttosfnt - osadzanie fontu bitmapowego w obudowie sfnt (TrueType)
Name:		xorg-app-fonttosfnt
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/fonttosfnt-%{version}.tar.bz2
# Source0-md5:	b0ebd86029571239b9d7b0c61191b591
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fonttosfnt application wraps a bitmap font or a set of bitmap fonts in
a sfnt (TrueType or OpenType) wrapper.

%description -l pl
Aplikacja fonttosfnt osadza font bitmapowy lub zbiór fontów
bitmapowych w obudowie sfnt (TrueType lub OpenType).

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/fonttosfnt
%{_mandir}/man1/fonttosfnt.1x*

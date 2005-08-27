Summary:	fonttosfnt application
Summary(pl):	Aplikacja fonttosfnt
Name:		xorg-app-fonttosfnt
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/fonttosfnt-%{version}.tar.bz2
# Source0-md5:	7c54c85ee877a9d6ca955ecc52995cf8
Patch0:		fonttosfnt-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-data-xbitmaps
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fonttosfnt application.

%description -l pl
Aplikacja fonttosfnt.

%prep
%setup -q -n fonttosfnt-%{version}
%patch0 -p1

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
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*

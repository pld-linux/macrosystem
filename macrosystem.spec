Summary:	MacroSystem
Name:		macrosystem
Version:	0.51
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/macrosystem/%{name}-%{version}.tar.gz
Patch0:		%{name}-c++.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MacroSystem is a powerful C++ template system designed to separate data
processing from content generation. With MacroSystem you can do recursive
macro replacing, nested if-else and ifnot-else constructs, easy importing
and exporting of macro files. It has been used to create dynamic web content,
email template systems, and many kinds of preprocessing utilities.

%package devel
Summary:	macrosystem - development files
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
macrosystem - development files.

%package static
Summary:	Static macrosystem library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static macrosystem library.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README examples
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.hh
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

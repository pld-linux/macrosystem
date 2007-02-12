Summary:	MacroSystem - powerful C++ template system
Summary(pl.UTF-8):   MacroSystem - potężny system szablonów C++
Name:		macrosystem
Version:	0.51
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/macrosystem/%{name}-%{version}.tar.gz
# Source0-md5:	5dbab1c8863888467a515650af96c710
Patch0:		%{name}-c++.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MacroSystem is a powerful C++ template system designed to separate
data processing from content generation. With MacroSystem you can do
recursive macro replacing, nested if-else and ifnot-else constructs,
easy importing and exporting of macro files. It has been used to
create dynamic web content, email template systems, and many kinds of
preprocessing utilities.

%description -l pl.UTF-8
MacroSystem to potężny system szablonów C++ opracowany, aby oddzielić
przetwarzanie danych od generowania treści. Przy użyciu MacroSystemu
można wykonywać rekurencyjne podstawianie makr, zagnieżdżone
konstrukcje if-else i ifnot-else, łatwe importowanie i eksportowanie
plików makr. System jest używany do tworzenia dynamicznej zawartości
stron WWW, systemów szablonów pocztowych oraz wielu rodzajów
narzędzi do preprocessingu.

%package devel
Summary:	MacroSystem - development files
Summary(pl.UTF-8):   MacroSystem - pliki dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
MacroSystem - development files.

%description devel -l pl.UTF-8
MacroSystem - pliki dla programistów.

%package static
Summary:	Static MacroSystem library
Summary(pl.UTF-8):   Statyczna biblioteka MacroSystem
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MacroSystem library.

%description static -l pl.UTF-8
Statyczna biblioteka MacroSystem.

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

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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

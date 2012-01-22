Summary:	Prints Excel spreadsheet (XLS, XLW) as a plain text
Name:		xls2txt
Version:	0.13
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://wizard.ae.krakow.pl/~jb/xls2txt/%{name}-%{version}.tar.gz
# Source0-md5:	5bb2ab2ab8dac7bfb34e2b536b399e12
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility prints Excel spreadsheet (XLS, XLW) as a plain text in
tab separated form.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fomit-frame-pointer" \
	LDFLAGS="%{rpmldflags}" \
	LDLIBS="-lm"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}

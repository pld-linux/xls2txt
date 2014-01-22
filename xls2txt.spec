Summary:	Print Excel spreadsheet (XLS, XLW) as a plain text
Summary(pl.UTF-8):	Wypisywanie arkuszy Excela (XLS, XLW) w postaci czystego tekstu
Name:		xls2txt
Version:	0.14
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://wizard.ae.krakow.pl/~jb/xls2txt/%{name}-%{version}.tar.gz
# Source0-md5:	166f73faac17248c5187b4c6029550bf
URL:		http://wizard.ae.krakow.pl/~jb/xls2txt/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This utility prints Excel spreadsheet (XLS, XLW) as a plain text in
tab separated form.

%description -l pl.UTF-8
To narzędzie wypisuje arkusze Excela (XLS, XLW) w postaci czystego
tekstu rozdzielonego tabulacjami.

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

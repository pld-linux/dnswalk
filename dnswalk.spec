#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
#
%include	/usr/lib/rpm/macros.perl
Summary:	The dnswalk DNS database debugger
Summary(pl):	Narzêdzie do diagnostyki baz danych DNS
Name:		dnswalk
Version:	2.0.2
Release:	0.2
License:	Artistic
Group:		Applications/Networking
Source0:	http://www.visi.com/~barr/dnswalk/%{name}-%{version}.tar.gz
# Source0-md5:	62b9302822353fad71d51aefdae1cad1
Patch0:		%{name}-perlpath.patch
Patch1:		%{name}-delete-filterout.patch
URL:		http://www.visi.com/~barr/dnswalk/
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps}
BuildRequires:	perl-Net-DNS
%endif
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dnswalk is a DNS debugger. It performs zone transfers of specified
domains, and checks the database in numerous ways for internal
consistency, as well as accuracy.

%description -l pl
dnswalk to narzêdzie do diagnostyki DNS-ów. Wykonuje transfery stref
dla podanych domen i sprawdza bazê danych w ró¿ny sposób pod k±tem
wewnêtrznej spójno¶ci oraz dok³adno¶ci.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p0

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}
install %{name} $RPM_BUILD_ROOT%{_sbindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO makereports sendreports rfc1912.txt do-dnswalk
%attr(755,root,root) %{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*

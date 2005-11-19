%global momorel 1

Summary:	The dnswalk DNS database debugger
Name:		dnswalk
Version:	2.0.2
Release:	%{momorel}m
Group:		Applications/Internet
URL:		http://www.visi.com/~barr/dnswalk/
License:	Artistic
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-perlpath.patch.bz2
Patch1:		%{name}-delete-filterout.patch.bz2
Requires:	perl-Net-DNS
Requires:	perl >= 5.004
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
dnswalk is a DNS debugger. It performs zone transfers of specified
domains, and checks the database in numerous ways for internal
consistency, as well as accuracy. 

%prep
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%setup -q -c -a0
%patch0 -p1
%patch1 -p0

%build

# fix attr
chmod 644 *

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man1
install -m755 %{name} %{buildroot}%{_sbindir}/
install -m755 %{name}.1 %{buildroot}%{_mandir}/man1/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README TODO makereports sendreports rfc1912.txt do-dnswalk
%attr(0755,root,root) %{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Jun 17 2005 TABUCHI Takaaki <tab@momonga-linux.org>
- (2.0.2-1m)
- adapt for momonga

* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.2-4mdk
- rebuild
- fix autodeps

* Sun May 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.2-3mdk
- build release

* Thu Jan 16 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.0.2-2mdk
- build release

* Sat Jun 29 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 2.0.2-1mdk
- initial cooker contrib

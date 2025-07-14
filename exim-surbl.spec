Summary:	Blocking Spam in Exim with URI Block Lists
Name:		exim-surbl
Version:	2.4
Release:	1
License:	GPL
Group:		Networking/Daemons/SMTP
Source0:	https://www.teuton.org/~ejm/exim_surbl/exim_surbl-%{version}.tar.gz
# Source0-md5:	8aefd22e5c19207b0452e75aa016020f
Patch0:		path.patch
Patch1:		config.patch
Patch2:		public_resolvers.patch
Patch3:		ip-meaning.patch
URL:		https://www.teuton.org/~ejm/exim_surbl/
Requires:	exim
Requires:	perl-Config-IniFiles
Requires:	perl-Net-DNS
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This document describes using SURBL (Spam URI Realtime Blocklists),
URIBL, and the Spamhaus DBL in conjunction with the Exim MTA to block
spam containing "spamvertizing" URLs. To achieve this, one can use the
Perl script that is found below. This utilizes Exim's MIME and/or DATA
ACLs and Exim's embedded Perl engine.

The Perl routine from this page should be relatively easy to modify to
use in any other MTA that can call an external script to scan a
message.

%prep
%setup -q -n exim_surbl-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

chmod 755 exim_surbl.pl
cp -p exim_surbl.pl $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -p config.ini surbl_whitelist.txt three-level-tlds two-level-tlds $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/exim_surbl.pl
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/config.ini
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/surbl_whitelist.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/three-level-tlds
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/two-level-tlds

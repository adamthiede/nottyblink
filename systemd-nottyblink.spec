Summary: a simple script to stop tty blinking
Name: systemd-nottyblink
Version: master
Release: 1%{?dist}
License: GPL
URL: https://git.sr.ht/~elagost/systemd-nottyblink
Source: https://git.sr.ht/~elagost/systemd-nottyblink/archive/master.tar.gz

BuildRequires: systemd

Requires: systemd bash

#%global debug_package %{nil}

%description
Stop TTY cursor blink with a service

%prep
%setup -q

%install
install -Dm755 systemd-nottyblink.sh %{buildroot}%{_bindir}/systemd-nottyblink.sh
install -Dm644 LICENSE %{buildroot}%{_datadir}/licenses/systemd-nottyblink/LICENSE
install -Dm644 systemd-nottyblink.service %{buildroot}%{_prefix}/lib/systemd/system/systemd-nottyblink.service
install -Dm644 cursor_blink.conf %{_sysconfigdir}/tmpfiles.d/cursor_blink.conf

%files
%{_bindir}/systemd-nottyblink.sh
%{_sysconfigdir}/tmpfiles.d/cursor_blink.conf
%{_prefix}/lib/systemd/system/systemd-nottyblink.service
%doc README.md
%license LICENSE

%changelog
* Mon Oct 31 2022 Adam Thiede <me@adamthiede.com>
- Created spec file

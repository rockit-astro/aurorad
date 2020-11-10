Name:      observatory-aurora-server
Version:   1.0.1
Release:   0
Url:       https://github.com/warwick-one-metre/aurora
Summary:   Weather station daemon for the Warwick La Palma telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-pyserial, python3-warwick-observatory-common, python3-warwick-observatory-aurora
Requires:  observatory-log-client, %{?systemd_requires}

%description
Part of the observatory software for the Warwick La Palma telescopes.

aurorad recieves data from a Eurotech Aurora Cloud Sensor III weather station attached via a USB-RS232 adaptor and
makes the latest measurement available for other services via Pyro.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_sysconfdir}/aurorad/

%{__install} %{_sourcedir}/aurorad %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/aurorad.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/10-superwasp-aurora.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/superwasp.json %{buildroot}%{_sysconfdir}/aurorad/

%post
%systemd_post aurorad.service

%preun
%systemd_preun aurorad.service

%postun
%systemd_postun_with_restart aurorad.service

%files
%defattr(0755,root,root,-)
%{_bindir}/aurorad
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-superwasp-aurora.rules
%{_unitdir}/aurorad.service
%{_sysconfdir}/aurorad/superwasp.json

%changelog

Name:      observatory-aurora-server
Version:   20220722
Release:   0
Url:       https://github.com/warwick-one-metre/aurorad
Summary:   Weather station daemon for the Warwick La Palma telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-pyserial python3-warwick-observatory-common python3-warwick-observatory-aurora

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_sysconfdir}/aurorad/

%{__install} %{_sourcedir}/aurorad %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/aurorad.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/10-superwasp-aurora.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/superwasp.json %{buildroot}%{_sysconfdir}/aurorad/

%files
%defattr(0755,root,root,-)
%{_bindir}/aurorad
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-superwasp-aurora.rules
%{_unitdir}/aurorad.service
%{_sysconfdir}/aurorad/superwasp.json

%changelog

Name:           python3-warwick-observatory-aurora
Version:        20220722
Release:        0
License:        GPL3
Summary:        Common backend code for the Aurora daemon.
Url:            https://github.com/warwick-one-metre/aurorad
BuildArch:      noarch

%description

%prep

rsync -av --exclude=build .. .

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog

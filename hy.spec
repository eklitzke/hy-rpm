# Created by pyp2rpm-3.3.2
%global pypi_name hy

Name:           %{pypi_name}
Version:        0.16.0
Release:        1%{?dist}
Summary:        Lisp and Python love each other

License:        Expat
URL:            http://hylang.org/
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(fastentrypoints)
BuildRequires:  python3dist(setuptools)

Requires:       python3dist(astor) >= 0.7.1
Requires:       python3dist(clint) >= 0.4
Requires:       python3dist(funcparserlib) >= 0.3.6
Requires:       python3dist(rply) >= 0.7.7
Requires:       python3dist(setuptools)
Requires:       python3dist(clint)
Requires:       python3dist(funcparserlib)

%description
Hy is a Python <--> Lisp layer. It helps make things work nicer, and lets
Python and the Hy lisp variant play nice together.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{_bindir}/hy
%{_bindir}/hy2py
%{_bindir}/hy2py3
%{_bindir}/hy3
%{_bindir}/hyc
%{_bindir}/hyc3
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Mar 26 2019 Evan Klitzke <evan@eklitzke.org> - 0.16.0-1
- Initial package.

%include	/usr/lib/rpm/macros.php
%define		_class		URI
%define		_subclass	Template
%define		_status		alpha
%define		_pearname	URI_Template
Summary:	%{_pearname} - Parser for URI Templates
Summary(pl.UTF-8):	%{_pearname} - parser szablonów URI
Name:		php-pear-%{_pearname}
Version:	0.3.1
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	432c823af101f6cc770c012daf98bebc
URL:		http://pear.php.net/package/URI_Template/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear >= 1.0-23
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
URI_Template is a parser for URI Templates as defined in the URI
Template specification (http://bitworking.org/projects/URI-Templates).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
URI_Template to parser szablonów URI zdefiniowanych w specyfikacji
szablonów URI (http://bitworking.org/projects/URI-Templates).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/URI/Template.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/URI_Template

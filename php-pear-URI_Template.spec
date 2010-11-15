%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	URI_Template
Summary:	%{_pearname} - Parser for URI Templates
Summary(pl.UTF-8):	%{_pearname} - parser szablonów URI
Name:		php-pear-%{_pearname}
Version:	0.3.2
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	fc0a736e50234500be8787c18236a08f
URL:		http://pear.php.net/package/URI_Template/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear >= 1.0-23
Obsoletes:	php-pear-URI_Template-tests
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

%prep
%pear_package_setup

# package maintainer helpers
rm .%{php_pear_dir}/URI/makepackage.php
rm .%{php_pear_dir}/data/URI_Template/runtests.sh

# duplicate bullshit
rm .%{php_pear_dir}/URI/URI/Template.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# tests should not be packaged
%{__rm} -r $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/URI/Template.php

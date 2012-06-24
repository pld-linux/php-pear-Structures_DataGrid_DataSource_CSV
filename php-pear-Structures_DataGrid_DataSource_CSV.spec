%include	/usr/lib/rpm/macros.php
%define		_class		Structures
%define		_subclass	DataGrid_DataSource_CSV
%define		_status		beta
%define		_pearname	Structures_DataGrid_DataSource_CSV

Summary:	%{_pearname} - DataSource driver using CSV files
Summary(pl):	%{_pearname} - sterownik DataSource dla plik�w CSV
Name:		php-pear-%{_pearname}
Version:	0.1.3
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	25bf3f307b35ffe3578ece71461d394d
URL:		http://pear.php.net/package/Structures_DataGrid_DataSource_CSV/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.4.-0.9
Requires:	php-pear-Structures_DataGrid >= 0.7.0
Requires:	php-pear-Structures_DataGrid_DataSource_Array >= 0.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a DataSource driver for Structures_DataGrid using CSV files.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet dostarcza sterownik DataSource do plik�w CSV dla
Structures_Datagrid.

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/Structures/DataGrid/DataSource/CSV.php

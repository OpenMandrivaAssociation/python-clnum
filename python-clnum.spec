%define module	clnum
%define name	python-%{module}
%define version 1.5
%define release 1

Summary:	Arbitrary precision floating point library for Python
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Source0:	%{module}-%{version}.tar.lzma
Patch0:		clnum.cpp.patch
License:	GPL
Group:		Development/Python 
Url: 		http://calcrpnpy.sourceforge.net/clnum.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	cln, python >= 2.0
BuildRequires:	cln-devel, python-devel >= 2.0

%description
The module clnum adds arbitrary precision floating point and rational
numbers to Python. Both real and complex types are supported. The
module also contains arbitrary precision replacements for the
functions in the standard library math and cmath modules.

The clnum module uses the Class Library for Numbers (CLN) to do all of
the hard work. The module simply provides a proper type interface so
that the CLN numbers work with the standard Python arithmetic
operators and interact properly with the built-in Python numeric
types.  

%prep 

%setup -q -n %{module}-%{version}
%patch0 -p0 

%build
%__python ./setup.py build

%install
%__rm -rf %{buildroot}
%__python ./setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README COPYING changelog *.html

%define module	clnum
%define debug_package %{nil}

Summary:	Arbitrary precision floating point library for Python
Name:		python-%{module}
Version:	1.6
Release:	5
Source0:	%{module}-%{version}.tar.gz
License:	GPL
Group:		Development/Python 
Url: 		http://calcrpnpy.sourceforge.net/clnum.html
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

%build
%__python ./setup.py build

%install
%__python ./setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%files
%doc README COPYING changelog *.html
%{py_platsitedir}/*

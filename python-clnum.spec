%define module	clnum
%define name	python-%{module}
%define version 1.6
%define rel 4

Summary:	Arbitrary precision floating point library for Python
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Source0:	%{module}-%{version}.tar.gz
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

%build
%__python ./setup.py build

%install
%__rm -rf %{buildroot}
%__python ./setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING changelog *.html
%py_platsitedir/*


%changelog
* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 1.6-4mdv2011.0
+ Revision: 598980
- rebuild for py2.7

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 1.6-3mdv2010.1
+ Revision: 503557
- rebuild for new gmp

* Wed Aug 05 2009 Funda Wang <fwang@mandriva.org> 1.6-2mdv2010.0
+ Revision: 410268
- rebuild for new cln

* Thu Apr 02 2009 Lev Givon <lev@mandriva.org> 1.6-1mdv2010.0
+ Revision: 363428
- Update to 1.6.

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1.5-2mdv2009.1
+ Revision: 323540
- rebuild

* Mon Oct 27 2008 Lev Givon <lev@mandriva.org> 1.5-1mdv2009.1
+ Revision: 297701
- Update to 1.5.

* Mon Jan 28 2008 Lev Givon <lev@mandriva.org> 1.4-5mdv2008.1
+ Revision: 159566
- Patch to build against cln 1.2.0.

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.4-4mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Jan 29 2007 Lev Givon <lev@mandriva.org> 1.4-4mdv2007.0
+ Revision: 115048
- Bump release.
- Specify Python version.

* Thu Jan 25 2007 Lev Givon <lev@mandriva.org> 1.4-3mdv2007.1
+ Revision: 113402
- Typo.
- Add python build dependency.

* Wed Jan 24 2007 Lev Givon <lev@mandriva.org> 1.4-2mdv2007.1
+ Revision: 113018
- Bump release.
- Update dependencies.

* Tue Jan 23 2007 Lev Givon <lev@mandriva.org> 1.4-1mdv2007.1
+ Revision: 112495
- Add build dependencies.
- Import python-clnum

* Fri Jan 19 2007 Lev Givon <lev@mandriva.org> 1.4-1mdv2007.0
- Update version.

* Thu May 25 2006 Lev Givon <lev@mandriva.org> 1.2-1mdk 
- Initial Mandriva package.


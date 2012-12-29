%define upstream_name geshi

Name:		php-%{upstream_name}
Version:	1.0.8.11
Release:	1
Summary:	Generic Syntax Highlighter
License:	PHP License
Group:		Development/PHP
URL:		http://qbnz.com/highlighter/
Source0:	https://sourceforge.net/projects/geshi/files/geshi/GeSHi%201.0.8.11/GeSHi-%{version}.tar.bz2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Generic Syntax Highlighter for PHP. Used to highlight almost any code
for the web. Nearly 100 supported languages: PHP, HTML, C and more. Styles can
be changed on the fly and CSS classes can be used to reduce the amount of XHTML
compliant output.

%prep
%setup -q -n %{upstream_name}

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_datadir}/php
cp -p geshi.php %{buildroot}%{_datadir}/php
cp -pr geshi %{buildroot}%{_datadir}/php
cp -pr contrib %{buildroot}%{_datadir}/php/geshi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs
%{_datadir}/php/*


%changelog
* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.8.10-3mdv2012.0
+ Revision: 761233
- rebuild

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.8.10-2
+ Revision: 695399
- rebuilt for php-5.3.7

* Fri Jul 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.8.10-1
+ Revision: 688447
- new version

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.8.8-4
+ Revision: 679256
- mass rebuild

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.8.8-3mdv2011.0
+ Revision: 629799
- rebuilt for php-5.3.5

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.8.8-2mdv2011.0
+ Revision: 600490
- rebuild

* Sat Aug 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.8.8-1mdv2011.0
+ Revision: 567295
- new version

* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.8.4-2mdv2010.0
+ Revision: 397149
- install under %%{_datadir}/php, so as to be automatically available in php include_path
- import php-geshi


* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.8.4-1mdv2010.0
- first mdv release


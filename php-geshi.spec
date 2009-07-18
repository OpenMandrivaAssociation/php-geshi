%define upstream_name geshi

Name:		php-%{upstream_name}
Version:	1.0.8.4
Release:	%mkrel 1
Summary:	Generic Syntax Highlighter
License:	PHP License
Group:		Development/PHP
URL:		http://qbnz.com/highlighter/
Source0:	http://sourceforge.net/projects/geshi/files/geshi/GeSHi-%{version}.tar.bz2
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
install -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -p geshi.php %{buildroot}%{_datadir}/%{name}
cp -pr geshi %{buildroot}%{_datadir}/%{name}
cp -pr contrib %{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs
%{_datadir}/%{name}


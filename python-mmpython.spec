#
# Conditional build:
%define		module	mmpython

Summary:	Media Metadata for Python
Name:		python-%{module}
Version:	0.4.5
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/mmpython
%pyrequires_eq	python-modules
BuildRequires:	glib-devel
BuildRequires:	python >= 2.2.1
BuildRequires:	rpm-pythonprov
BuildRequires:	python-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Media Metadata for Python

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{py_sitedir}/%{module}/*

%define		module	mmpython
Summary:	Media Metadata for Python
Summary(pl):	Metadane multimedialne dla Pythona
Name:		python-%{module}
Version:	0.4.5
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/mmpython/%{module}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/mmpython/
%pyrequires_eq	python-modules
BuildRequires:	glib-devel
BuildRequires:	python >= 2.2.1
BuildRequires:	rpm-pythonprov
BuildRequires:	python-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MMPython is a Media Meta Data retrieval framework. It retrieves
metadata from mp3, ogg, avi, jpg, tiff and other file formats. Among
others it thereby parses ID3v2, ID3v1, EXIF, IPTC and Vorbis data into
an object oriented struture.

%description -l pl
MMPython to szkielet do odczytywania metadanych z multimediów.
Odtwarza metadane z plików mp3, ogg, avi, jpg, tiff i innych formatów.
Miêdzy innymi przetwarza dane ID3v2, TD3v1, EXIF, IPTC i Vorbis na
struktury zorientowane obiektowo.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}" \
python setup.py build

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
%{py_sitedir}/%{module}

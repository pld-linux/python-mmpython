%define		module	mmpython
Summary:	Media Metadata for Python
Summary(pl.UTF-8):	Metadane multimedialne dla Pythona
Name:		python-%{module}
Version:	0.4.9
Release:	8
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/mmpython/%{module}-%{version}.tar.gz
# Source0-md5:	f95699c2f4249d21105d7977a15d5dcc
Patch0:		%{name}-intypes.patch
URL:		http://sourceforge.net/projects/mmpython/
BuildRequires:	libdvdread-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
Requires:	python-PyXML
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MMPython is a Media Meta Data retrieval framework. It retrieves
metadata from MP3, Ogg, AVI, JPG, TIFF and other file formats. Among
others it thereby parses ID3v2, ID3v1, EXIF, IPTC and Vorbis data into
an object oriented struture.

%description -l pl.UTF-8
MMPython to szkielet do odczytywania metadanych z multimediów.
Odtwarza metadane z plików MP3, Ogg, AVI, JPG, TIFF i innych formatów.
Między innymi przetwarza dane ID3v2, TD3v1, EXIF, IPTC i Vorbis na
struktury zorientowane obiektowo.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--install-platlib=%{py_sitescriptdir}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{module}

%define		module	mmpython
Summary:	Media Metadata for Python
Summary(pl):	Metadane multimedialne dla Pythona
Name:		python-%{module}
Version:	0.4.7
Release:	2
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/mmpython/%{module}-%{version}.tar.gz
# Source0-md5:	fbd0fb7bc855e0b9f31485c9f9c256a7
URL:		http://sourceforge.net/projects/mmpython/
%pyrequires_eq	python-modules
BuildRequires:	libdvdread-devel
BuildRequires:	python >= 2.2.1
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MMPython is a Media Meta Data retrieval framework. It retrieves
metadata from MP3, Ogg, AVI, JPG, TIFF and other file formats. Among
others it thereby parses ID3v2, ID3v1, EXIF, IPTC and Vorbis data into
an object oriented struture.

%description -l pl
MMPython to szkielet do odczytywania metadanych z multimediów.
Odtwarza metadane z plików MP3, Ogg, AVI, JPG, TIFF i innych formatów.
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
	--root=$RPM_BUILD_ROOT \
	--install-platlib=%{py_sitescriptdir} \
	--install-purelib=%{py_sitedir}

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*py -exec rm -f \{\} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{module}

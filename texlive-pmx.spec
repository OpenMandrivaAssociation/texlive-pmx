Name:		texlive-pmx
Version:	62533
Release:	1
Summary:	Preprocessor for MusiXTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/pmx
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pmx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pmx.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-pmx.bin

%description
PMX is a preprocessor for MusiXTeX. It builds the TeX input
file from a file in a much simpler language, making most of the
layout decisions by itself. An auxiliary program makes single-
player parts from a multi-player score. For proof-listening,
PMX can make a MIDI file of your score. The present version
requires at least version 1.15 of MusiXTeX, running on an e-
tex-enhanced TeX system.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pmx
%doc %{_texmfdistdir}/doc/generic/pmx
%doc %{_mandir}/man1/pmxab.1*
%doc %{_texmfdistdir}/doc/man/man1/pmxab.man1.pdf
%doc %{_mandir}/man1/scor2prt.1*
%doc %{_texmfdistdir}/doc/man/man1/scor2prt.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1

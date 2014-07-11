# revision 33826
# category Package
# catalog-ctan /support/pmx
# catalog-date 2013-12-16 11:52:21 +0100
# catalog-license gpl2
# catalog-version 2.7.0
Name:		texlive-pmx
Version:	2.7.0
Release:	9
Summary:	Preprocessor for MusiXTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/pmx
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pmx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pmx.doc.tar.xz
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
%{_texmfdistdir}/scripts/pmx/pmx2pdf.lua
%{_texmfdistdir}/tex/generic/pmx/pmx.tex
%doc %{_texmfdistdir}/doc/generic/pmx/README
%doc %{_texmfdistdir}/doc/generic/pmx/examples/barsant.pmx
%doc %{_texmfdistdir}/doc/generic/pmx/examples/dyntest.pmx
%doc %{_texmfdistdir}/doc/generic/pmx/examples/most.pmx
%doc %{_texmfdistdir}/doc/generic/pmx/examples/mwalmnd.pmx
%doc %{_texmfdistdir}/doc/generic/pmx/file600.eps
%doc %{_texmfdistdir}/doc/generic/pmx/gpl.txt
%doc %{_texmfdistdir}/doc/generic/pmx/install_run_pmx270.pdf
%doc %{_texmfdistdir}/doc/generic/pmx/install_run_pmx270.tex
%doc %{_texmfdistdir}/doc/generic/pmx/pmx-install.pdf
%doc %{_texmfdistdir}/doc/generic/pmx/pmx-install.tex
%doc %{_texmfdistdir}/doc/generic/pmx/pmx25-27.html
%doc %{_texmfdistdir}/doc/generic/pmx/pmx270.pdf
%doc %{_texmfdistdir}/doc/generic/pmx/pmx270.tex
%doc %{_texmfdistdir}/doc/generic/pmx/pmx2pdf.html
%doc %{_texmfdistdir}/doc/generic/pmx/pmxab.html
%doc %{_texmfdistdir}/doc/generic/pmx/ref270.pdf
%doc %{_texmfdistdir}/doc/generic/pmx/ref270.tex
%doc %{_texmfdistdir}/doc/generic/pmx/scor2prt.html
%doc %{_mandir}/man1/pmx2pdf.1*
%doc %{_texmfdistdir}/doc/man/man1/pmx2pdf.man1.pdf
%doc %{_mandir}/man1/pmxab.1*
%doc %{_texmfdistdir}/doc/man/man1/pmxab.man1.pdf
%doc %{_mandir}/man1/scor2prt.1*
%doc %{_texmfdistdir}/doc/man/man1/scor2prt.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1

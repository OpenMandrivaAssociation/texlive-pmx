# revision 26689
# category Package
# catalog-ctan /support/pmx
# catalog-date 2012-04-10 15:56:49 +0200
# catalog-license gpl2
# catalog-version 2.6.18
Name:		texlive-pmx
Version:	2.6.18
Release:	2
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
%{_texmfdistdir}/scripts/pmx/Windows/pmx2pdf.bat
%{_texmfdistdir}/scripts/pmx/pmx2pdf.lua
%{_texmfdistdir}/tex/generic/pmx/pmx.tex
%doc %{_texmfdistdir}/doc/generic/pmx/examples/barsant.pmx
%doc %{_texmfdistdir}/doc/generic/pmx/examples/dyntest.pmx
%doc %{_texmfdistdir}/doc/generic/pmx/examples/most.pmx
%doc %{_texmfdistdir}/doc/generic/pmx/examples/mwalmnd.pmx
%doc %{_texmfdistdir}/doc/generic/pmx/file600.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmx260.pdf
%doc %{_texmfdistdir}/doc/generic/pmx/pmx260.tex
%doc %{_texmfdistdir}/doc/generic/pmx/pmx2pdf.1
%doc %{_texmfdistdir}/doc/generic/pmx/pmx2pdf.pdf
%doc %{_texmfdistdir}/doc/generic/pmx/pmxab.1
%doc %{_texmfdistdir}/doc/generic/pmx/pmxab.pdf
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/README
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/addresses/btennent.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/addresses/cmondrup.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/addresses/dlaurie.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/addresses/dsimons.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/addresses/hmorimoto.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/addresses/jpcoulon.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/addresses/mcodogno.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/addresses/noack.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/addresses/ovogel.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/addresses/rdunker.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/addresses/skneifl.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/addresses/texmusiclist.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/14.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/18.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/19.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/20.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/21k.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/21m.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/21n.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/22.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/22k.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/22m.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/22n.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/27.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/27a.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/28.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/29.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/29a.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/29b.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/29c.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/34.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/Donjump.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/Haydn.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/JChrBach.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/MIDI.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/MIDIbaroque.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/agon.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/autobeam.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/bars.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/beams.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/beethoven0.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/beethoven1.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/bloch.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/bruckner.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/caccini1.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/caccini2.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/caccini3.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/chords.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/chordslur.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/clefchg.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/clefchg2.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/clefnot.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/cslurs1k.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/cslurs1m.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/cslurs1n.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/cslurs2k.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/cslurs2m.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/cslurs2n.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/debussy.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/diabolca.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/diabolica.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/dottedslur.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/dufay.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/grace.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/inlinesample.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/jumpbeam.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/jumpslur.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/keychg.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/kslurs1.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/kslurs2.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/kslurtweaks.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/macro.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/meter.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/mozart.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/mtrauermus.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/notepara.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/noteparb.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/noteparc.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/ornament.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/pathetique.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/pickups.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/pitch.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/poppea.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/reloctav.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/rests.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/samp-eps.zip
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/slurs1.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/slurs2.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/transpose.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/transpose1.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/transpose2.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/transpose3.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/triplerest.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/tristano.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/tristans.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/tristn.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/trists.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/vivaldi1.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/vivaldi2.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/volta.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/xtupletrest.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/xtuplets.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/eps/xtupletsSich.eps
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/pmxccn2618.pdf
%doc %{_texmfdistdir}/doc/generic/pmx/pmxccn/pmxccn2618.tex
%doc %{_texmfdistdir}/doc/generic/pmx/ref260.pdf
%doc %{_texmfdistdir}/doc/generic/pmx/ref260.tex
%doc %{_texmfdistdir}/doc/generic/pmx/scor2prt.1
%doc %{_texmfdistdir}/doc/generic/pmx/scor2prt.pdf
%doc %{_texmfdistdir}/doc/support/pmx/ChangeLog
%doc %{_texmfdistdir}/doc/support/pmx/OSX/pmxab
%doc %{_texmfdistdir}/doc/support/pmx/OSX/scor2prt
%doc %{_texmfdistdir}/doc/support/pmx/README
%doc %{_texmfdistdir}/doc/support/pmx/pmx-install.pdf
%doc %{_texmfdistdir}/doc/support/pmx/pmx-install.tex
%doc %{_mandir}/man1/pmx2pdf.1*
%doc %{_texmfdir}/doc/man/man1/pmx2pdf.man1.pdf
%doc %{_mandir}/man1/pmxab.1*
%doc %{_texmfdir}/doc/man/man1/pmxab.man1.pdf
%doc %{_mandir}/man1/scor2prt.1*
%doc %{_texmfdir}/doc/man/man1/scor2prt.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -r texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1/

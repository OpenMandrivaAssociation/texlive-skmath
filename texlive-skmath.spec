# revision 30941
# category Package
# catalog-ctan /macros/latex/contrib/skmath
# catalog-date 2013-06-24 23:09:25 +0200
# catalog-license lppl1.3
# catalog-version 0.3a
Name:		texlive-skmath
Version:	0.3a
Release:	8
Summary:	Extensions to the maths command repertoir
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/skmath
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skmath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skmath.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skmath.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a selection of new maths commands and
improved re-definitions of existing commands.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/skmath/skmath.sty
%doc %{_texmfdistdir}/doc/latex/skmath/README
%doc %{_texmfdistdir}/doc/latex/skmath/skmath.pdf
#- source
%doc %{_texmfdistdir}/source/latex/skmath/skmath.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

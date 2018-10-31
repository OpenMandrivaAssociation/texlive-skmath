Name:		texlive-skmath
Version:	0.4b
Release:	2
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
%{_texmfdistdir}/tex/latex/skmath
%doc %{_texmfdistdir}/doc/latex/skmath
#- source
%doc %{_texmfdistdir}/source/latex/skmath

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

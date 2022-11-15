Name:		texlive-bussproofs-extra
Version:	51299
Release:	1
Summary:	Extra commands for bussproofs.sty
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bussproofs-extra
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bussproofs-extra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bussproofs-extra.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bussproofs-extra.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides additional functionality for
bussproofs.sty; specifically, it allows for typesetting of
entire (sub)deductions.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/bussproofs-extra
%{_texmfdistdir}/tex/latex/bussproofs-extra
%doc %{_texmfdistdir}/doc/latex/bussproofs-extra

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

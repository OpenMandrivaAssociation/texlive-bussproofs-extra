%global tl_name bussproofs-extra
%global tl_revision 51299

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Extra commands for bussproofs.sty
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bussproofs-extra
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bussproofs-extra.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bussproofs-extra.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bussproofs-extra.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides additional functionality for bussproofs.sty;
specifically, it allows for typesetting of entire (sub)deductions.


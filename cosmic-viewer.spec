%undefine _debugsource_packages
%global appid com.system76.CosmicViewer

Name:           cosmic-viewer
Version:        1.11.0
Release:        %{?beta:0.%{beta}.}1
Summary:        COSMIC Image Viewer
Group:          Desktop/COSMIC
License:	GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-viewer
Source0:        https://github.com/pop-os/cosmic-viewer/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  just
BuildRequires:  rust-packaging
BuildRequires:  rust >= 1.93
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake
BuildRequires:  nasm
BuildRequires:  make

%description
COSMIC Image Viewer.

%prep
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/metainfo/%{appid}.metainfo.xml


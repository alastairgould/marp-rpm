%global _opt /opt

Name:          marp 
Version:       0.0.11
Release:       1%{?dist}
Summary:       Markdown Presentation Writer 
Group:         Development Tools

URL:           https://github.com/yhatt/marp 
License:       MIT
Source0:       https://github.com/yhatt/marp/releases/download/v%{version}/%{version}-Marp-linux-x64.tar.gz 
BuildRequires: desktop-file-utils
Autoreq: 0

%description
Markdown presentation writer, powered by Electron.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_opt}/%{name}
tar -xf %{SOURCE0} --directory %{buildroot}/%{_opt}/%{name}/ --mode=755
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications marp.desktop

%files
/%{_opt}/%{name}/
/%{_datadir}/applications/

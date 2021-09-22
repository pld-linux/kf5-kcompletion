# TODO:
# - runtime Requires if any
%define		kdeframever	5.86
%define		qtver		5.15.2
%define		kfname		kcompletion

Summary:	String completion framework
Name:		kf5-%{kfname}
Version:	5.86.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	8457c5c1e0336fe85ebbc11bdf68d41b
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt5Widgets >= %{qtver}
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
This class offers "auto-completion", "manual-completion" or "shell
completion" on QString objects. A common use is completing filenames
or URLs. It can also be used for completing email-addresses,
telephone-numbers, commands, SQL queries, etc.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Widgets-devel >= %{qtver}
Requires:	cmake >= 3.16

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}5_qt --with-qm --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5_qt.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %ghost %{_libdir}/libKF5Completion.so.5
%attr(755,root,root) %{_libdir}/libKF5Completion.so.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/kcompletion5widgets.so
%{_datadir}/qlogging-categories5/kcompletion.categories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KCompletion
%{_includedir}/KF5/kcompletion_version.h
%{_libdir}/cmake/KF5Completion
%{_libdir}/libKF5Completion.so
%{qt5dir}/mkspecs/modules/qt_KCompletion.pri

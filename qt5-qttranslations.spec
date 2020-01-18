
%global qt_module qttranslations

#define prerelease

Summary: Qt5 - QtTranslations module
Name:    qt5-%{qt_module}
Version: 5.6.1
Release: 10%{?prerelease:.%{prerelease}}%{?dist}

License: LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
Url:     http://www.qt.io
Source0: http://download.qt.io/snapshots/qt/5.6/%{version}%{?prerelease:-%{prerelease}}/submodules/%{qt_module}-opensource-src-%{version}%{?prerelease:-%{prerelease}}.tar.xz
BuildArch: noarch
%global _qt5_qmake %{_bindir}/qmake-qt5

BuildRequires: qt5-qtbase-devel >= %{version}
# for lrelease
BuildRequires: qt5-linguist

# help system-config-language and dnf/yum langpacks pull these in
%if 0%{?_qt5:1}
Provides: %{_qt5}-ar = %{version}-%{release}
Provides: %{_qt5}-ca = %{version}-%{release}
Provides: %{_qt5}-cs = %{version}-%{release}
Provides: %{_qt5}-da = %{version}-%{release}
Provides: %{_qt5}-de = %{version}-%{release}
Provides: %{_qt5}-es = %{version}-%{release}
Provides: %{_qt5}-fa = %{version}-%{release}
Provides: %{_qt5}-fi = %{version}-%{release}
Provides: %{_qt5}-fr = %{version}-%{release}
Provides: %{_qt5}-gl = %{version}-%{release}
Provides: %{_qt5}-he = %{version}-%{release}
Provides: %{_qt5}-hu = %{version}-%{release}
Provides: %{_qt5}-it = %{version}-%{release}
Provides: %{_qt5}-ja = %{version}-%{release}
Provides: %{_qt5}-ko = %{version}-%{release}
Provides: %{_qt5}-lt = %{version}-%{release}
Provides: %{_qt5}-lv = %{version}-%{release}
Provides: %{_qt5}-pl = %{version}-%{release}
Provides: %{_qt5}-pt = %{version}-%{release}
Provides: %{_qt5}-ru = %{version}-%{release}
Provides: %{_qt5}-sk = %{version}-%{release}
Provides: %{_qt5}-sl = %{version}-%{release}
Provides: %{_qt5}-sv = %{version}-%{release}
Provides: %{_qt5}-uk = %{version}-%{release}
Provides: %{_qt5}-zh_CN = %{version}-%{release}
Provides: %{_qt5}-zh_TW = %{version}-%{release}
%endif

%description
%{summary}.


%prep
%setup -q -n %{qt_module}-opensource-src-%{version}%{?prerelease:-%{prerelease}}


%build
%{qmake_qt5}
make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot}

# not used currently, since we track locales manually to keep %%files/Provides sync'd -- rex
#find_lang qttranslations --all-name --with-qt --without-mo


%files
%doc LICENSE.LGPL* LGPL_EXCEPTION.txt
%lang(ar) %{_qt5_translationdir}/*_ar.qm
%lang(ca) %{_qt5_translationdir}/*_ca.qm
%lang(cs) %{_qt5_translationdir}/*_cs.qm
%lang(da) %{_qt5_translationdir}/*_da.qm
%lang(de) %{_qt5_translationdir}/*_de.qm
%lang(es) %{_qt5_translationdir}/*_es.qm
%lang(en) %{_qt5_translationdir}/*_en.qm
%lang(fa) %{_qt5_translationdir}/*_fa.qm
%lang(fi) %{_qt5_translationdir}/*_fi.qm
%lang(fr) %{_qt5_translationdir}/*_fr.qm
%lang(gl) %{_qt5_translationdir}/*_gl.qm
%lang(he) %{_qt5_translationdir}/*_he.qm
%lang(hu) %{_qt5_translationdir}/*_hu.qm
%lang(it) %{_qt5_translationdir}/*_it.qm
%lang(ja) %{_qt5_translationdir}/*_ja.qm
%lang(ko) %{_qt5_translationdir}/*_ko.qm
%lang(lt) %{_qt5_translationdir}/*_lt.qm
%lang(lt) %{_qt5_translationdir}/*_lv.qm
%lang(pl) %{_qt5_translationdir}/*_pl.qm
%lang(pt) %{_qt5_translationdir}/*_pt.qm
%lang(ru) %{_qt5_translationdir}/*_ru.qm
%lang(sk) %{_qt5_translationdir}/*_sk.qm
%lang(sl) %{_qt5_translationdir}/*_sl.qm
%lang(sv) %{_qt5_translationdir}/*_sv.qm
%lang(uk) %{_qt5_translationdir}/*_uk.qm
%lang(zh_CN) %{_qt5_translationdir}/*_zh_CN.qm
%lang(zh_TW) %{_qt5_translationdir}/*_zh_TW.qm


%changelog
* Tue Aug 30 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.1-10
- Increase build version to have newer version than in EPEL
  Resolves: bz#1317414

* Wed Jun 08 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.1-1
- Update to 5.6.1
  Resolves: bz#1317414

* Thu Apr 07 2016 Jan Grulich <jgrulich@redhat.com> - 5.6.0-2
- Initial version for RHEL
  Resolves: bz#1317414

* Mon Mar 14 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-1
- 5.6.0 final release

* Tue Feb 23 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.7.rc
- Update to final RC

* Mon Feb 15 2016 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.6
- Update RC release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Rex Dieter <rdieter@fedoraproject.org> 5.6.0-0.4
- drop BR: pkgconfig(Qt5Help), drop unused %%find_lang

* Sat Jan 23 2016 Rex Dieter <rdieter@fedoraproject.org> 5.6.0-0.3
- use %%qmake_qt5 (and hack around %%_qt5_qmake noarch issue)

* Thu Dec 10 2015 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.2
- Official rc release

* Tue Nov 03 2015 Helio Chissini de Castro <helio@kde.org> - 5.6.0-0.1
- Start to implement 5.6.0 rc

* Thu Oct 15 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.1-2
- Update to final release 5.5.1

* Tue Sep 29 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.1-1
- Update to Qt 5.5.1 RC1

* Wed Jul 29 2015 Rex Dieter <rdieter@fedoraproject.org> 5.5.0-2
- BR: qt5-linguist, relax qt5-qttools dep

* Thu Jun 25 2015 Helio Chissini de Castro <helio@kde.org> - 5.5.0-0.2.rc
- Update for official RC1 released packages

* Wed Jun 17 2015 Daniel Vrátil <dvratil@redhat.com> - 5.5.0-0.1.rc
- Qt 5.5.0 RC1

* Thu Jun 04 2015 Jan Grulich <jgrulich@redhat.com> 5.4.2-1
- 5.4.2

* Thu Mar 26 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.1-2
- Provides: qt5-qtbase-<locales> to aid dnf/yum langpacks plugin and system-config-language (#1170730)

* Tue Feb 24 2015 Jan Grulich <jgrulich@redhat.com> 5.4.1-1
- 5.4.1

* Wed Dec 10 2014 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-1
- 5.4.0 (final)

* Fri Nov 28 2014 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-0.2.rc
- 5.4.0-rc

* Mon Oct 20 2014 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-0.1.rc
- 5.4.0-rc

* Wed Sep 17 2014 Rex Dieter <rdieter@fedoraproject.org> - 5.3.2-1
- 5.3.2

* Tue Jun 17 2014 Jan Grulich <jgrulich@redhat.com> - 5.3.1-1
- 5.3.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jan Grulich <jgrulich@redhat.com> 5.3.0-1
- 5.3.0

* Wed Feb 05 2014 Rex Dieter <rdieter@fedoraproject.org> 5.2.1-1
- 5.2.1

* Thu Dec 12 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-1
- 5.2.0

* Mon Dec 02 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-0.10.rc1
- 5.2.0-rc1

* Thu Oct 24 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-0.2.rc1
- 5.2.0-rc1

* Wed Oct 02 2013 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-0.1.alpha
- 5.2.0-alpha

* Sun Sep 22 2013 Rex Dieter <rdieter@fedoraproject.org> 5.1.1-1
- Initial packaging

#
# spec file for package nagios-plugin-check_newest_file_age
#

Name:           nagios-plugin-check_newest_file_age
Version:        %{version}
Release:        %{release}
Summary:        Checks newest file in directory
License:        MIT License
Group:          System/Monitoring
Url:            https://github.com/joernott/nagios-plugin-newest-file-age
Source0:        nagios-plugin-check_newest_file_age-%{version}.tar.gz
Requires:       nagios-plugins
BuildArch:      noarch
Provides:       check_newest_file_age

%description
This plugin pulls the most recently created file in each specified directory,
and checks its created time against the current time. If the maximum age of
the file is exceeded, a warning/critical message is returned as appropriate.

This is useful for examining backup directories for freshness.

%prep
%setup -q -n nagios-plugin-newest-file-age-%{version}

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT/usr/lib64/nagios/plugins"
cp check_newest_file_age "$RPM_BUILD_ROOT/usr/lib64/nagios/plugins/"

%files
%defattr(-,root,root,755)
%attr(0755,root,root) /usr/lib64/nagios/plugins/check_newest_file_age

%doc README.md LICENSE

%changelog
* Wed Apr 27 2022 Joern Ott <joern.ott@ott-consult.de>
- Add build script and SPEC
- Fix #17: correctly check files with space in its filename 
- fix #14, fix #16: Return UNKNOWN on ls command error 

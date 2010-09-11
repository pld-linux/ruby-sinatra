
%define gitrev c496254
%define gitauthor sinatra
%define pkgname sinatra

Summary:	Classy web-development dressed in a DSL
Name:		ruby-%{pkgname}
Version:	1.0
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://download.github.com/%{gitauthor}-%{pkgname}-%{version}-0-g%{gitrev}.tar.gz
# Source0-md5:	c0f9693865054a453120d9ebb7a21000
URL:		http://sinatrarb.com/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby
BuildRequires:	ruby-modules
BuildRequires:	setup.rb = 3.4.1
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sinatra is a DSL for quickly creating web applications in Ruby with
minimal effort

%prep
%setup -q -n %{gitauthor}-%{pkgname}-%{gitrev}
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--installdirs=std
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/sinatra.rb
%{ruby_rubylibdir}/sinatra

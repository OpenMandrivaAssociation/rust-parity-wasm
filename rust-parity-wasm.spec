# Generated by rust2rpm-9-1.fc31
%bcond_with check
%global debug_package %{nil}

%global crate parity-wasm

Name:           rust-%{crate}
Version:        0.38.0
Release:        3%{?dist}
Summary:        WebAssembly binary format serialization/deserialization/interpreter

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/parity-wasm
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
%if %{with check}
BuildRequires:  (crate(time/default) >= 0.1.0 with crate(time/default) < 0.2.0)
%endif

%global _description \
WebAssembly binary format serialization/deserialization/interpreter.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
# https://github.com/paritytech/parity-wasm/issues/224
%cargo_test -- --doc
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.38.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 15:34:26 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.38.0-1
- Update to 0.38.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.35.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.35.7-1
- Update to 0.35.7

* Tue Jan 08 2019 Josh Stone <jistone@redhat.com> - 0.35.6-1
- Update to 0.35.6

* Thu Dec 06 2018 Josh Stone <jistone@redhat.com> - 0.35.4-1
- Update to 0.35.4

* Thu Nov 29 2018 Josh Stone <jistone@redhat.com> - 0.35.3-1
- Update to 0.35.3

* Thu Nov 29 2018 Josh Stone <jistone@redhat.com> - 0.35.2-1
- Update to 0.35.2

* Tue Nov 27 2018 Josh Stone <jistone@redhat.com> - 0.35.1-1
- Update to 0.35.1

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.34.0-1
- Update to 0.34.0

* Sun Sep 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.32.0-1
- Initial package

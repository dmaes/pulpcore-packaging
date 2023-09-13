%{?python_disable_dependency_generator}
%global pypi_name opentelemetry_exporter_otlp

Name:           python-%{pypi_name}
Version:        1.19.0
Release:        2%{?dist}
Summary:        OpenTelemetry Collector Exporters

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/blob/v1.19.0/exporter/opentelemetry-exporter-otlp/
Source:         https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-opentelemetry_exporter_otlp_proto_grpc >= 1.19.0
Requires:       python%{python3_pkgversion}-opentelemetry_exporter_otlp_proto_http >= 1.19.0

%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/
%{python3_sitelib}/opentelemetry/exporter/otlp

%changelog
* Tue Aug 08 2023 Odilon Sousa <osousa@redhat.com> - 1.19.0-2
- Update opentelemetry dependency names

* Wed Jul 26 2023 Odilon Sousa - 1.19.0-1
- Initial package.
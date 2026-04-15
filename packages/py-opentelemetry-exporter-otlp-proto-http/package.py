# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOpentelemetryExporterOtlpProtoHttp(PythonPackage):
    """OpenTelemetry Collector OTLP exporter over HTTP."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-otlp-proto-http"
    pypi = "opentelemetry-exporter-otlp-proto-http/opentelemetry_exporter_otlp_proto_http-1.33.0.tar.gz"

    license("Apache-2.0")

    version("1.33.0", sha256="bf0cf7568432621b903223e5b72aa9f8fe425fcc748e54d0b21ebe99885c12ee")
    version("1.27.0", sha256="2103479092d8eb18f61f3fbff084f67cc7f2d4a7d37e75304b8b56c1d09ebef5")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-deprecated@1.2.6:", type=("build", "run"))
    depends_on("py-googleapis-common-protos@1.52:1", type=("build", "run"))
    depends_on("py-requests@2.7:2", type=("build", "run"))
    depends_on("py-opentelemetry-exporter-otlp-proto-common@1.27.0", when="@1.27.0", type=("build", "run"))
    depends_on("py-opentelemetry-exporter-otlp-proto-common@1.33.0", when="@1.33.0", type=("build", "run"))
    depends_on("py-opentelemetry-proto@1.27.0", when="@1.27.0", type=("build", "run"))
    depends_on("py-opentelemetry-proto@1.33.0", when="@1.33.0", type=("build", "run"))
    depends_on("py-opentelemetry-sdk@1.27.0", when="@1.27.0", type=("build", "run"))
    depends_on("py-opentelemetry-sdk@1.33.0", when="@1.33.0", type=("build", "run"))
    depends_on("py-opentelemetry-api@1.27.0", when="@1.27.0", type=("build", "run"))
    depends_on("py-opentelemetry-api@1.33.0", when="@1.33.0", type=("build", "run"))
    depends_on("py-opentelemetry-semantic-conventions", type=("build", "run"))

    def patch(self):
        filter_file(r'^\s*"Framework :: [^\n]*\n', "", "pyproject.toml")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python(
                "-c",
                "from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter",
            )

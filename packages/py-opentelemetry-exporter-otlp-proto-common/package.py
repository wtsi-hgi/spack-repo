# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOpentelemetryExporterOtlpProtoCommon(PythonPackage):
    """Shared OTLP protobuf helpers for OpenTelemetry exporters."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-otlp-proto-common"
    pypi = "opentelemetry-exporter-otlp-proto-common/opentelemetry_exporter_otlp_proto_common-1.33.0.tar.gz"

    license("Apache-2.0")

    version("1.33.0", sha256="2f43679dab68ce7708db18cb145b59a7e9184d46608ef037c9c22f47c5beb320")
    version("1.27.0", sha256="159d27cf49f359e3798c4c3eb8da6ef4020e292571bd8c5604a2a573231dd5c8")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-opentelemetry-proto@1.27.0", when="@1.27.0", type=("build", "run"))
    depends_on("py-opentelemetry-proto@1.33.0", when="@1.33.0", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import opentelemetry.exporter.otlp.proto.common")

# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOpentelemetryInstrumentationHttpx(PythonPackage):
    """HTTPX client instrumentation for OpenTelemetry."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-httpx"
    pypi = "opentelemetry-instrumentation-httpx/opentelemetry_instrumentation_httpx-0.54b0.tar.gz"

    license("Apache-2.0")

    version("0.54b0", sha256="1db2e949d627654462dd129e6342cc8119bed6cd376df60ae7e92f6a47bede26")
    version("0.48b0", sha256="ee977479e10398931921fb995ac27ccdeea2e14e392cb27ef012fc549089b60a")

    depends_on("py-hatchling", type="build")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-opentelemetry-api@1.12:", type=("build", "run"))
    depends_on("py-opentelemetry-instrumentation@0.48b0", when="@0.48b0", type=("build", "run"))
    depends_on("py-opentelemetry-instrumentation@0.54b0", when="@0.54b0", type=("build", "run"))
    depends_on(
        "py-opentelemetry-semantic-conventions@0.48b0",
        when="@0.48b0",
        type=("build", "run"),
    )
    depends_on(
        "py-opentelemetry-semantic-conventions@0.54b0",
        when="@0.54b0",
        type=("build", "run"),
    )
    depends_on("py-opentelemetry-util-http@0.48b0", when="@0.48b0", type=("build", "run"))
    depends_on("py-opentelemetry-util-http@0.54b0", when="@0.54b0", type=("build", "run"))
    depends_on("py-wrapt@1.0.0:2.0.0", when="@0.54b0", type=("build", "run"))
    depends_on("py-httpx@0.18:", type=("build", "run"))

    def patch(self):
        filter_file(r'^\s*"Framework :: OpenTelemetry",\n', "", "pyproject.toml")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python(
                "-c",
                "from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor",
            )

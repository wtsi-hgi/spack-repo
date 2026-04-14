# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOpentelemetryInstrumentationUrllib(PythonPackage):
    """urllib instrumentation for OpenTelemetry."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-urllib"
    pypi = "opentelemetry-instrumentation-urllib/opentelemetry_instrumentation_urllib-0.54b0.tar.gz"

    license("Apache-2.0")

    version("0.54b0", sha256="f95d7718d41952326b496577b143e6e8daa9ec213cd62e09ba2c6a77c2252735")
    version("0.48b0", sha256="a9db839b4248efc9b01628dc8aa886c1269a81cec84bc375d344239037823d48")

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

    def patch(self):
        filter_file(r'^\s*"Framework :: OpenTelemetry",\n', "", "pyproject.toml")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python(
                "-c",
                "from opentelemetry.instrumentation.urllib import URLLibInstrumentor",
            )

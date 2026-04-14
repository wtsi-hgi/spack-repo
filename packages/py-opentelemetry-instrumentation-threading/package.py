# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOpentelemetryInstrumentationThreading(PythonPackage):
    """Thread context propagation helpers for OpenTelemetry."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-threading"
    pypi = "opentelemetry-instrumentation-threading/opentelemetry_instrumentation_threading-0.54b0.tar.gz"

    license("Apache-2.0")

    version("0.54b0", sha256="74677085514d0f3a0f77593fc515812f6048ec47023e618ee02c6d80ad02306a")
    version("0.48b0", sha256="daef8a6fd06aa8b35594582d96ffb30954c4a9ae1ffdace7b00d0904fd650d2e")

    depends_on("py-hatchling", type="build")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-opentelemetry-api@1.12:", type=("build", "run"))
    depends_on("py-opentelemetry-instrumentation@0.48b0", when="@0.48b0", type=("build", "run"))
    depends_on("py-opentelemetry-instrumentation@0.54b0", when="@0.54b0", type=("build", "run"))
    depends_on("py-wrapt@1.0.0:2.0.0", type=("build", "run"))

    def patch(self):
        filter_file(r'^\s*"Framework :: OpenTelemetry",\n', "", "pyproject.toml")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python(
                "-c",
                "from opentelemetry.instrumentation.threading import ThreadingInstrumentor",
            )

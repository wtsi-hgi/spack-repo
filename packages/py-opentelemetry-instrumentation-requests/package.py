# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOpentelemetryInstrumentationRequests(PythonPackage):
    """Requests instrumentation for OpenTelemetry."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-requests"
    pypi = "opentelemetry-instrumentation-requests/opentelemetry_instrumentation_requests-0.54b0.tar.gz"

    license("Apache-2.0")

    version("0.54b0", sha256="abc604d58a0da9cbfad2e9439df2b85437ec00bf550753cf64bf6d61e2b98bdd")
    version("0.48b0", sha256="67ab9bd877a0352ee0db4616c8b4ae59736ddd700c598ed907482d44f4c9a2b3")

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
    depends_on("py-requests@2:", type=("build", "run"))

    def patch(self):
        filter_file(r'^\s*"Framework :: OpenTelemetry",\n', "", "pyproject.toml")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python(
                "-c",
                "from opentelemetry.instrumentation.requests import RequestsInstrumentor",
            )

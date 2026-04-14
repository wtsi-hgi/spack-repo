# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpentelemetryInstrumentation(PythonPackage):
    """Convenience tooling that automatically instruments supported libraries."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/opentelemetry-instrumentation"
    pypi = "opentelemetry_instrumentation/opentelemetry_instrumentation-0.54b0.tar.gz"

    license("Apache-2.0")

    version("0.54b0", sha256="2949d0bbf2316eb5d928a5ef610d0a8a2c261ba80167d878abf6016e1c4ae7bb")
    version("0.48b0", sha256="94929685d906380743a71c3970f76b5f07476eea1834abd5dd9d17abfe23cc35")
    version("0.42b0", sha256="6a653a1fed0f76eea32885321d77c750483e987eeefa4cbf219fc83559543198")

    depends_on("py-hatchling", type="build")
    depends_on("python@3.8:", when="@0.48b0:", type=("build", "run"))
    depends_on("py-setuptools@16:", when="@0.48b0:", type="build")
    depends_on("py-opentelemetry-api@1.4:", type=("build", "run"))
    depends_on("py-opentelemetry-semantic-conventions@0.48b0", when="@0.48b0", type=("build", "run"))
    depends_on("py-opentelemetry-semantic-conventions@0.54b0", when="@0.54b0", type=("build", "run"))
    depends_on("py-packaging@18:", when="@0.54b0", type=("build", "run"))
    depends_on("py-wrapt@1.0.0:2.0.0", type=("build", "run"))

    def patch(self):
        if self.spec.satisfies("@0.48b0:"):
            filter_file(r'^\s*"Framework :: OpenTelemetry",\n', "", "pyproject.toml")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import opentelemetry.instrumentation")

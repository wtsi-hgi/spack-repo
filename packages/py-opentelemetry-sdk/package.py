# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpentelemetrySdk(PythonPackage):
    """OpenTelemetry Python SDK."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python"
    pypi = "opentelemetry_sdk/opentelemetry_sdk-1.33.0.tar.gz"

    license("Apache-2.0")

    version("1.33.0", sha256="a7fc56d1e07b218fcc316b24d21b59d3f1967b2ca22c217b05da3a26b797cc68")
    version("1.27.0", sha256="d525017dea0ccce9ba4e0245100ec46ecdc043f2d7b8315d56b19aff0904fa6f")
    version("1.21.0", sha256="3ec8cd3020328d6bc5c9991ccaf9ae820ccb6395a5648d9a95d3ec88275b8879")

    depends_on("py-hatchling", type="build")
    depends_on("python@3.8:", when="@1.27:", type=("build", "run"))
    depends_on("py-opentelemetry-api", when="@:1.26", type=("build", "run"))
    depends_on("py-opentelemetry-api@1.27.0", when="@1.27:1.32", type=("build", "run"))
    depends_on("py-opentelemetry-api@1.33.0", when="@1.33:", type=("build", "run"))
    depends_on("py-opentelemetry-semantic-conventions", when="@:1.26", type=("build", "run"))
    depends_on("py-opentelemetry-semantic-conventions@0.48b0", when="@1.27:1.32", type=("build", "run"))
    depends_on("py-opentelemetry-semantic-conventions@0.54b0", when="@1.33:", type=("build", "run"))
    depends_on("py-typing-extensions@3.7.4:", type=("build", "run"))

    def patch(self):
        if self.spec.satisfies("@1.27:"):
            filter_file(r'^\s*"Framework :: OpenTelemetry",\n', "", "pyproject.toml")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "from opentelemetry import sdk")

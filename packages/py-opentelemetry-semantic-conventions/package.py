# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOpentelemetrySemanticConventions(PythonPackage):
    """Generated code for the semantic conventions defined by the OpenTelemetry specification."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-semantic-conventions"
    pypi = "opentelemetry_semantic_conventions/opentelemetry_semantic_conventions-0.54b0.tar.gz"

    license("Apache-2.0")

    version("0.54b0", sha256="467b739977bdcb079af1af69f73632535cdb51099d5e3c5709a35d10fe02a9c9")
    version("0.48b0", sha256="12d74983783b6878162208be57c9effcb89dc88691c64992d70bb89dc00daa1a")
    version("0.42b0", sha256="44ae67a0a3252a05072877857e5cc1242c98d4cf12870159f1a94bec800d38ec")

    depends_on("python@3.8:", type=("build", "run"), when="@0.48b0:")
    depends_on("py-hatchling", type="build")
    depends_on("py-opentelemetry-api@1.27.0", when="@0.48b0", type=("build", "run"))
    depends_on("py-opentelemetry-api@1.33.0", when="@0.54b0", type=("build", "run"))
    depends_on("py-deprecated@1.2.6:", when="@0.48b0:", type=("build", "run"))

    def patch(self):
        if self.spec.satisfies("@0.48b0:"):
            filter_file(r'^\s*"Framework :: OpenTelemetry",\n', "", "pyproject.toml")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "from opentelemetry import semconv")

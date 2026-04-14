# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpentelemetryApi(PythonPackage):
    """OpenTelemetry Python API."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-api"
    pypi = "opentelemetry_api/opentelemetry_api-1.33.0.tar.gz"

    license("Apache-2.0")

    version("1.33.0", sha256="cc4380fd2e6da7dcb52a828ea81844ed1f4f2eb638ca3c816775109d93d58ced")
    version("1.27.0", sha256="ed673583eaa5f81b5ce5e86ef7cdaf622f88ef65f0b9aab40b843dcae5bef342")
    version("1.21.0", sha256="d6185fd5043e000075d921822fd2d26b953eba8ca21b1e2fa360dd46a7686316")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-importlib-metadata@6.0:7", when="@:1.26", type=("build", "run"))
    depends_on("py-importlib-metadata@6.0:8.4", when="@1.27:1.32", type=("build", "run"))
    depends_on("py-importlib-metadata@6.0:8.6", when="@1.33:", type=("build", "run"))
    depends_on("py-deprecated@1.2.6:", when="@1.27:", type=("build", "run"))

    def patch(self):
        if self.spec.satisfies("@1.27:"):
            filter_file(r'^\s*"Framework :: OpenTelemetry",\n', "", "pyproject.toml")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import opentelemetry")

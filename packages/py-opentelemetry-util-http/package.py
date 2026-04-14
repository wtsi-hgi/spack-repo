# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOpentelemetryUtilHttp(PythonPackage):
    """Utility helpers shared by the OpenTelemetry HTTP instrumentations."""

    homepage = "https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/util/opentelemetry-util-http"
    pypi = "opentelemetry-util-http/opentelemetry_util_http-0.54b0.tar.gz"

    license("Apache-2.0")

    version("0.54b0", sha256="2b5fe7157928bdbde194d38df7cbd35a679631fe5b6c23b2c4a271229f7e42b5")
    version("0.48b0", sha256="60312015153580cc20f322e5cdc3d3ecad80a71743235bdb77716e742814623c")

    depends_on("py-hatchling", type="build")
    depends_on("python@3.8:", type=("build", "run"))

    def patch(self):
        filter_file(r'^\s*"Framework :: OpenTelemetry",\n', "", "pyproject.toml")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import opentelemetry.util.http")

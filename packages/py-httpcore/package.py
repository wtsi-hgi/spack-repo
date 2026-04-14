# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHttpcore(PythonPackage):
    """Minimal, low-level HTTP client used underneath HTTPX."""

    homepage = "https://github.com/encode/httpcore"
    pypi = "httpcore/httpcore-1.0.9.tar.gz"

    license("BSD-3-Clause")

    version("1.0.9", sha256="6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8")
    version("1.0.5", sha256="34a38e2f9291467ee3b44e89dd52615370e152954ba21721378a87b2960f7a61")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-fancy-pypi-readme", type="build")
    depends_on("py-certifi", type=("build", "run"))
    depends_on("py-h11@0.16:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import httpcore")

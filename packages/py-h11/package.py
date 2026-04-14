# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyH11(PythonPackage):
    """Pure-Python, bring-your-own-I/O HTTP/1.1 protocol implementation."""

    homepage = "https://github.com/python-hyper/h11"
    pypi = "h11/h11-0.16.0.tar.gz"

    license("MIT")

    version("0.16.0", sha256="4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import h11")

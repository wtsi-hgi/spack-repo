# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPot(PythonPackage):
    """Python Optimal Transport Library."""

    homepage = "https://github.com/PythonOT/POT"
    pypi = "POT/pot-0.9.7.post1.tar.gz"

    license("MIT")

    version("0.9.7.post1", sha256="2edd70845047ac2d378487b980a2bffb5ff58e9b92b7133896ff5753f6300cec")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools@42:", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-cython@0.23:", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy@1.6:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        python = which(self.spec["python"].command.path)
        with working_dir("spack-test", create=True):
            python("-c", "import ot")

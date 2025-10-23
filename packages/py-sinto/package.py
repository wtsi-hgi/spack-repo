# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySinto(PythonPackage):
    """Tools for single-cell data processing"""

    homepage = "https://timoast.github.io/sinto/"
    pypi = "sinto/sinto-0.10.1.tar.gz"

    license("MIT")

    version("0.10.1", sha256="ac54280a62db55d139635cf96a2a36e40857282f660a67c1ce5d4a31115beae7")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pysam@0.14:", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-umi-tools", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            sinto = Executable(join_path(self.prefix.bin, "sinto"))
            sinto("--help")

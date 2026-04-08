# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySswPy(PythonPackage):
    """Python bindings for the Complete-Striped-Smith-Waterman-Library (SSW)."""

    homepage = "https://github.com/libnano/ssw-py"
    pypi = "ssw-py/ssw-py-1.0.1.tar.gz"

    license("MIT")

    version("1.0.1", sha256="11e8eb4aa0c42cff31908869f69b6d233f1600273698a792ced355bd18e23ec0")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools@65.6.3:", type="build")
    depends_on("py-cython", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import ssw; ssw.AlignmentMgr")

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTreelib(PythonPackage):
    """Python implementation of a tree data structure."""

    homepage = "https://github.com/caesar0301/treelib"
    pypi = "treelib/treelib-1.8.0.tar.gz"

    version("1.8.0", sha256="e1be2c6b66ffbfae85079fc4c76fb4909946d01d915ee29ff6795de53aed5d55")

    license("Apache-2.0")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-poetry-core", type="build")
    depends_on("py-six@1.13:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import treelib")

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGraphtools(PythonPackage):
    """Tools for building and manipulating graphs in Python.."""

    homepage = "https://github.com/KrishnaswamyLab/graphtools"
    pypi = "graphtools/graphtools-1.5.3.tar.gz"

    license("GPL-2.0-only")

    version("2.1.0", sha256="ffeeb042b927422c990233e51fb7fe0afb42c4345ec1ca1d8926d9a0e6bd0fe8")
    version("1.5.3", sha256="b35ae2974d24c507fe01b110d10b1d8c949e20bc49ff9d7d04f94849f9795907")
    
    depends_on("python@3.5:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.14.0:", type=("build", "run"))
    depends_on("py-scipy@1.1.0:", type=("build", "run"))
    depends_on("py-pygsp@0.5.1:", type=("build", "run"))
    depends_on("py-scikit-learn@0.20.0:", type=("build", "run"))
    depends_on("py-future", type=("build", "run"))
    depends_on("py-tasklogger@1.0:", type=("build", "run"))
    depends_on("py-deprecated", type=("build", "run"))
    
    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import graphtools")

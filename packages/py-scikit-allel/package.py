# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScikitAllel(PythonPackage):
    """Exploratory analysis toolkit for large-scale genetic variation data."""

    homepage = "https://github.com/cggh/scikit-allel"
    pypi = "scikit-allel/scikit_allel-1.3.13.tar.gz"

    version("1.3.13", sha256="9a38b4cc00d3ba9ad997aaa57d0f03f3331e4771e3889f0d9c584a0d7f533e35")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-cython@0.29:", type="build")
    depends_on("py-setuptools-scm+toml", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-dask+array", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import allel")

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScikitAllel(PythonPackage):
    """A Python package for exploratory analysis of large scale genetic variation data."""

    homepage = "https://github.com/cggh/scikit-allel"
    pypi = "scikit-allel/scikit-allel-1.3.7.tar.gz"

    version("1.3.7", sha256="cb6229c407451bf1ea4b7fa681188e142d24a3a168ca6e786b6b4a7e999507f4")

    depends_on("py-cython", type=("build", "run"))
    depends_on("py-setuptools-scm", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-dask+array", type=("build", "run"))
    depends_on("py-nose", type=("run"))
    depends_on("py-scipy", type=("run"))
    depends_on("py-matplotlib", type=("run"))
    depends_on("py-seaborn", type=("run"))
    depends_on("py-pandas", type=("run"))
    depends_on("py-pomegranate", type=("run"))
    depends_on("py-scikit-learn", type=("run"))
    depends_on("py-h5py", type=("run"))
    depends_on("py-numexpr", type=("run"))
    depends_on("py-numcodecs", type=("run"))
    depends_on("py-zarr", type=("run"))
    depends_on("py-hmmlearn", type=("run"))
    depends_on("py-pytest", type=("run"))
    depends_on("py-ipython", type=("run"))

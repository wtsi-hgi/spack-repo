# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBbknn(PythonPackage):
    """BBKNN is a fast and intuitive batch effect removal tool that can be directly used in the scanpy workflow."""

    homepage = "https://github.com/Teichlab/bbknn"
    pypi = "bbknn/bbknn-1.6.0.tar.gz"

    version("1.6.0", sha256="1c01a9d6df2fc52a527de8a403617897a4b672724863299a7026f2132f1b041b")

    depends_on("py-flit-core", type="build")

    depends_on("py-cython", type=("build", "run"))
    depends_on("py-scipy@1.6.0:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-annoy", type=("build", "run"))
    depends_on("py-pynndescent", type=("build", "run"))
    depends_on("py-umap-learn", type=("build", "run"))
    depends_on("py-scikit-learn@1.0.2:", type=("build", "run"))

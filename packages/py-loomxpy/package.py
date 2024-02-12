# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLoomxpy(PythonPackage):
    """Python package (compatible with SCope) to create .loom files and extend them with other data e.g.: SCENIC regulons."""

    homepage = "https://github.com/aertslab/LoomXpy"
    pypi = "loomxpy/loomxpy-0.4.2.tar.gz"

    version("0.4.2", sha256="188411b77e04fa8458c0a7f02cfb3f15b58410a020f81f522957e922e79cdd82")

    depends_on("py-poetry", type="build")
    depends_on("py-poetry-core", type="build")

    depends_on("py-loompy@3.0.7", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pyscenic@0.12.0:", type=("build", "run"))
    depends_on("py-scikit-learn@0.22.2:", type=("build", "run"))
    depends_on("py-ctxcore@0.2.0:", type=("build", "run"))

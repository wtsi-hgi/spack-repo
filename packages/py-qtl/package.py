# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQtl(PythonPackage):
    """pyQTL is a python module for analyzing and visualizing quantitative trait loci (QTL) data."""

    homepage = "https://github.com/broadinstitute/pyqtl"
    pypi = "qtl/qtl-0.1.8.tar.gz"

    version("0.1.8", sha256="8fdb99cda1ceff578a233db6c15a944fa57b43a2826af41c292e36848906117b")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-pybigwig", type=("build", "run"))
    depends_on("py-bx-python", type=("build", "run"))

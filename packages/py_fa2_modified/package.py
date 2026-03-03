# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFa2Modified(PythonPackage):
    """A port of Gephi's Force Atlas 2 layout algorithm to Python 3 (with a wrapper for NetworkX and igraph). This is the fastest python implementation available with most of the features complete. It also supports Barnes Hut approximation for maximum speedup. For Python3.9+."""

    homepage = "https://github.com/AminAlam/fa2_modified"
    pypi = "fa2_modified/fa2_modified-0.3.10.tar.gz"

    version("0.3.10", sha256="6e527bbec70454dc3f85ffeb651a0e293540f4fc83ca98fac0aeb55211322f4e")

    depends_on("python@3.9:", type=("build", "run"))
    # depends_on("py-setuptools", type="build")

    depends_on("py-igraph", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))

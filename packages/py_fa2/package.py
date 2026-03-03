# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFa2(PythonPackage):
    """A port of Gephi's Force Atlas 2 layout algorithm to Python 2 and Python 3 (with a wrapper for NetworkX and igraph). This is the fastest python implementation available with most of the features complete. It also supports Barnes Hut approximation for maximum speedup."""

    homepage = "https://github.com/bhargavchippada/forceatlas2"
    pypi = "fa2/fa2-0.3.5.tar.gz"

    version("0.3.5", sha256="9a12e0a7dc228999c605beaae751424ec4a4f60281f44683c0744a72fc9141ef")

    depends_on("python@3:3.9", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-igraph", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))

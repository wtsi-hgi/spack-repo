# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSanta(RPackage):
    """Spatial Analysis of Network Associations

    This package provides methods for measuring the strength of association between a network and a phenotype. It does this by measuring clustering of the phenotype across the network (Knet). Vertices can also be individually ranked by their strength of association with high-weight vertices (Knode).
    """

    bioc = "SANTA"

    version("2.44.0", commit="496edf66ce5145651a02ab937a2a2e9ac9a8fb3b")
    version("2.38.0", commit="d7a133ab17f6b64f02efd853c34e6d55d87d1fb5")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbh(RPackage):
    """Interaction Based Homogeneity for Evaluating Gene Lists

    This package contains methods for calculating Interaction Based Homogeneity to evaluate fitness of gene lists to an interaction network which is useful for evaluation of clustering results and gene list analysis. BioGRID interactions are used in the calculation. The user can also provide their own interactions.
    """

    bioc = "ibh"

    version("1.56.0", commit="9e4677deb05764dce3ebec9c4cd1aed66de6e037")
    version("1.50.0", commit="2604376ba090a6ee3c7bb38e37ee716b6a265063")

    depends_on("r-simpintlists", type=("build", "run"))

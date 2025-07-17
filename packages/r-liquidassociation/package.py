# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiquidassociation(RPackage):
    """LiquidAssociation

    The package contains functions for calculate direct and model-based estimators for liquid association. It also provides functions for testing the existence of liquid association given a gene triplet data.
    """

    bioc = "LiquidAssociation"

    version("1.62.0", commit="a39c6740a26b5782c596584f01e9cace2e231f6a")
    version("1.56.0", commit="66e5dfc6190e54da5fca061a77bec0ad89f869c3")

    depends_on("r-geepack", type=("build", "run"))
    depends_on("r-yeastcc", type=("build", "run"))
    depends_on("r-org-sc-sgd-db", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))

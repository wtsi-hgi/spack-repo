# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogicfs(RPackage):
    """Identification of SNP Interactions

    Identification of interactions between binary variables using Logic Regression. Can, e.g., be used to find interesting SNP interactions. Contains also a bagging version of logic regression for classification.
    """

    bioc = "logicFS"

    version("2.28.0", commit="21132df49df7e1384473cff3f1c67470ea1978ee")
    version("2.22.0", commit="c976e6430d38fb464fcd63a013c531bc823dcdd3")

    depends_on("r-logicreg", type=("build", "run"))
    depends_on("r-mcbiopi", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastliquidassociation(RPackage):
    """functions for genome-wide application of Liquid Association

    This package extends the function of the LiquidAssociation package for genome-wide application. It integrates a screening method into the LA analysis to reduce the number of triplets to be examined for a high LA value and provides code for use in subsequent significance analyses.
    """

    bioc = "fastLiquidAssociation"

    version("1.44.0", commit="1a4a255d9f154eaa51dbf08a7f975f7bfbf72a70")
    version("1.38.0", commit="664f7f2c296c2f4a9ea7fec532a3a97cd272dced")

    depends_on("r-liquidassociation", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-wgcna", type=("build", "run"))
    depends_on("r-impute", type=("build", "run"))
    depends_on("r-preprocesscore", type=("build", "run"))

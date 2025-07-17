# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCafe(RPackage):
    """Chromosmal Aberrations Finder in Expression data

    Detection and visualizations of gross chromosomal aberrations using Affymetrix expression microarrays as input
    """

    bioc = "CAFE"

    version("1.44.0", commit="d293796bbc2eafdb812b064545e68db488dd3a7a")
    version("1.38.0", commit="ecba1e78e873bb127725c25cf5e24c6a3196addc")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biovizbase", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-ggbio", type=("build", "run"))
    depends_on("r-affy", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-annotate", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))

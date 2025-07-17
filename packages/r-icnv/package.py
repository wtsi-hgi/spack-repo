# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcnv(RPackage):
    """Integrated Copy Number Variation detection

    Integrative copy number variation (CNV) detection from multiple platform and experimental design.
    """

    bioc = "iCNV"

    version("1.28.0", commit="ceaff487dd6c5c53dd62e6af3045e9c6f992efd8")
    version("1.22.0", commit="7b945291253842a7be96e46eb14b29e4ec53e03d")

    depends_on("r@3.3.1:", type=("build", "run"))
    depends_on("r-codex", type=("build", "run"))
    depends_on("r-fields", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-truncnorm", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))

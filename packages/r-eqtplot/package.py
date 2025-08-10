# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REqtplot(RPackage):
    """Visualization of Colocalization Between eQTL and GWAS Data.

    eQTpLot is an R package for visualizing colocalization, correlation, and
    enrichment between eQTL and GWAS signals for a given gene-trait pair.
    """

    homepage = "https://github.com/RitchieLab/eQTpLot"
    git = "https://github.com/RitchieLab/eQTpLot.git"

    license("GPL-3.0")

    # No tagged releases. Use latest known commit with date-based version.
    version("20220513", commit="ef6289c4f2fa06d5deb820891624798c1bf2e09f")

    # Core R version requirement
    depends_on("r@3.5.0:", type=("build", "run"))

    # Depends
    depends_on("r-ggplot2@3.3.0:", type=("build", "run"))

    # Imports listed in DESCRIPTION/README
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
    depends_on("r-ggnewscale", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-ggpubr", type=("build", "run"))
    depends_on("r-ggplotify", type=("build", "run"))
    depends_on("r-ldheatmap", type=("build", "run"))
    depends_on("r-viridislite", type=("build", "run"))


# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDegreport(RPackage):
    """Creation of a HTML report of differential expression analyses of count data."""

    homepage = "http://lpantano.github.io/DEGreport/"
    url = "https://www.bioconductor.org/packages/release/bioc/src/contrib/DEGreport_1.36.0.tar.gz"
    bioc = "DEGreport"

    version("1.36.0", sha256="51edcd04b8a272b38c361d865c1b91b7c0df70c12e28201057dfeb87050db597")

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-broom", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-consensusclusterplus", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggdendro", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-logging", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-psych", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-reshape", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))

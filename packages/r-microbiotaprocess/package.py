# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobiotaprocess(RPackage):
    """A comprehensive R package for managing and analyzing microbiome and other ecological data within the tidy framework

    MicrobiotaProcess is an R package for analysis, visualization and biomarker discovery of microbial datasets. It introduces MPSE class, this make it more interoperable with the existing computing ecosystem. Moreover, it introduces a tidy microbiome data structure paradigm and analysis grammar. It provides a wide variety of microbiome data analysis procedures under the unified and common framework (tidy-like framework).
    """

    homepage = "https://github.com/YuLab-SMU/MicrobiotaProcess/"
    bioc = "MicrobiotaProcess"

    version("1.20.1", commit="c6d9972ebce9b72454bb33605f1eea5872aaec95")
    version("1.14.1", commit="9fc267f6d1f60cd3d8bc7a38efc7fddb5f84278a")
    version("1.14.0", md5="104b99004b64b664131ddea6462cbabc")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-vegan", type=("build", "run"))
    depends_on("r-zoo", type=("build", "run"))
    depends_on("r-ggtree", type=("build", "run"))
    depends_on("r-tidytree@0.4.2:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-coin", type=("build", "run"))
    depends_on("r-ggsignif", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-ggstar", type=("build", "run"))
    depends_on("r-tidyselect", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-treeio@1.17.2:", type=("build", "run"))
    depends_on("r-pillar", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-dtplyr", type=("build", "run"))
    depends_on("r-ggtreeextra", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-ggfun@0.1.1:", type=("build", "run"))

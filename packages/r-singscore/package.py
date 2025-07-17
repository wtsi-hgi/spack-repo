# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSingscore(RPackage):
    """Rank-based single-sample gene set scoring method

    A simple single-sample gene signature scoring method that uses rank-based statistics to analyze the sample's gene expression profile. It scores the expression activities of gene sets at a single-sample level.
    """

    homepage = "https://davislaboratory.github.io/singscore"
    bioc = "singscore"

    version("1.28.0", commit="9f4d8bac8062f1b27770fac46a877ab3c6357423")
    version("1.22.0", commit="1941ad87ec156b1e3ad45aad0d0f147e8a1e4ff6")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-gseabase", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-reshape", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))

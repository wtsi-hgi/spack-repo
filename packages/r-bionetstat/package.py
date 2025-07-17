# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBionetstat(RPackage):
    """Biological Network Analysis

    A package to perform differential network analysis, differential node analysis (differential coexpression analysis), network and metabolic pathways view.
    """

    homepage = "http://github.com/jardimViniciusC/BioNetStat"
    bioc = "BioNetStat"

    version("1.22.0", commit="f29e4164f0ab0e80f2f2da3a3047a099efe05c80")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-shinybs", type=("build", "run"))
    depends_on("r-pathview", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-rjsonio", type=("build", "run"))
    depends_on("r-whisker", type=("build", "run"))
    depends_on("r-yaml", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-psych", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-markdown", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioconcotk(RPackage):
    """Bioconductor components for general cancer genomics

    Provide a central interface to various tools for genome-scale analysis of cancer studies.
    """

    bioc = "BiocOncoTK"
    urls = [
        "https://bioconductor.org/packages/release/bioc/src/contrib/BiocOncoTK_1.24.0.tar.gz",
    ]
    version("1.24.0", sha256="a3ae5bb9a251ee9122de9a14fb770e206f5d8e73470724db3cddaf9ae9c98c40")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-bigrquery", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-rjson", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-curatedtcgadata", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-ggpubr", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-car", type=("build", "run"))
    depends_on("r-graph", type=("build", "run"))
    depends_on("r-rgraphviz", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))

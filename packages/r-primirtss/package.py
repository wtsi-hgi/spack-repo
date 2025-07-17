# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrimirtss(RPackage):
    """Prediction of pri-miRNA Transcription Start Site

    A fast, convenient tool to identify the TSSs of miRNAs by integrating the data of H3K4me3 and Pol II as well as combining the conservation level and sequence feature, provided within both command-line and graphical interfaces, which achieves a better performance than the previous non-cell-specific methods on miRNA TSSs.
    """

    homepage = "https://github.com/ipumin/primirTSS"
    bioc = "primirTSS"

    version("1.26.0", commit="63d93c515ebf81fa49e8765475639339c71e08cc")
    version("1.20.0", commit="8fd698e09c8a75ce759d56e677bc27bea53de53e")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicranges@1.32.2:", type=("build", "run"))
    depends_on("r-s4vectors@0.18.2:", type=("build", "run"))
    depends_on("r-rtracklayer@1.40.3:", type=("build", "run"))
    depends_on("r-dplyr@0.7.6:", type=("build", "run"))
    depends_on("r-stringr@1.3.1:", type=("build", "run"))
    depends_on("r-tidyr@0.8.1:", type=("build", "run"))
    depends_on("r-biostrings@2.48:", type=("build", "run"))
    depends_on("r-purrr@0.2.5:", type=("build", "run"))
    depends_on("r-bsgenome-hsapiens-ucsc-hg38@1.4.1:", type=("build", "run"))
    depends_on("r-phastcons100way-ucsc-hg38@3.7.1:", type=("build", "run"))
    depends_on("r-genomicscores@1.4.1:", type=("build", "run"))
    depends_on("r-shiny@1.0.5:", type=("build", "run"))
    depends_on("r-gviz@1.24:", type=("build", "run"))
    depends_on("r-biocgenerics@0.26:", type=("build", "run"))
    depends_on("r-iranges@2.14.10:", type=("build", "run"))
    depends_on("r-tfbstools@1.18:", type=("build", "run"))
    depends_on("r-jaspar2018@1.1.1:", type=("build", "run"))
    depends_on("r-tibble@1.4.2:", type=("build", "run"))
    depends_on("r-r-utils@2.6:", type=("build", "run"))

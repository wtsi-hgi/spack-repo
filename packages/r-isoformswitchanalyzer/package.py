# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsoformswitchanalyzer(RPackage):
    """Identify, Annotate and Visualize Isoform Switches with Functional Consequences from both short- and long-read RNA-seq data

    Analysis of alternative splicing and isoform switches with predicted functional consequences (e.g. gain/loss of protein domains etc.) from quantification of all types of RNASeq by tools such as Kallisto, Salmon, StringTie, Cufflinks/Cuffdiff etc.
    """

    homepage = "http://bioconductor.org/packages/IsoformSwitchAnalyzeR/"
    bioc = "IsoformSwitchAnalyzeR"

    version("2.8.0", commit="b2397a013063c49427410413507ea3b851873937")
    version("2.2.0", commit="172bcd11235943c418a894b1107fb650818f5a10")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-dexseq", type=("build", "run"))
    depends_on("r-saturn@1.7:", type=("build", "run"))
    depends_on("r-sva", type=("build", "run"))
    depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
    depends_on("r-pfamanalyzer", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-biostrings@2.50:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-venndiagram", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-tximport@1.7.1:", type=("build", "run"))
    depends_on("r-tximeta@1.7.12:", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-futile-logger", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-xvector", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))

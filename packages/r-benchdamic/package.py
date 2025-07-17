# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBenchdamic(RPackage):
    """Benchmark of differential abundance methods on microbiome data

    Starting from a microbiome dataset (16S or WMS with absolute count values) it is possible to perform several analysis to assess the performances of many differential abundance detection methods. A basic and standardized version of the main differential abundance analysis methods is supplied but the user can also add his method to the benchmark. The analyses focus on 4 main aspects: i) the goodness of fit of each method's distributional assumptions on the observed count data, ii) the ability to control the false discovery rate, iii) the within and between method concordances, iv) the truthfulness of the findings if any apriori knowledge is given. Several graphical functions are available for result visualization.
    """

    bioc = "benchdamic"

    version("1.14.2", commit="9ea0f3adc92ea88f5d0ff7225899a068bbc0c3ff")
    version("1.8.2", commit="c22b1934ea56333035188a8124dd37a2b3ac3c2d")
    version("1.8.1", md5="ca158383ebf87138c91438c7946fe567")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-phyloseq", type=("build", "run"))
    depends_on("r-treesummarizedexperiment", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-zinbwave", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-aldex2", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-mast", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-ancombc", type=("build", "run"))
    depends_on("r-mixomics", type=("build", "run"))
    depends_on("r-lme4", type=("build", "run"))
    depends_on("r-noiseq", type=("build", "run"))
    depends_on("r-dearseq", type=("build", "run"))
    depends_on("r-microbiomestat", type=("build", "run"))
    depends_on("r-maaslin2", type=("build", "run"))
    depends_on("r-gunifrac", type=("build", "run"))
    depends_on("r-metagenomeseq", type=("build", "run"))
    depends_on("r-mglm", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-ggdendro", type=("build", "run"))
    depends_on("r-ggridges", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-tidytext", type=("build", "run"))

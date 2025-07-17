# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDamirseq(RPackage):
    """Data Mining for RNA-seq data: normalization, feature selection and classification

    The DaMiRseq package offers a tidy pipeline of data mining procedures to identify transcriptional biomarkers and exploit them for both binary and multi-class classification purposes. The package accepts any kind of data presented as a table of raw counts and allows including both continous and factorial variables that occur with the experimental setting. A series of functions enable the user to clean up the data by filtering genomic features and samples, to adjust data by identifying and removing the unwanted source of variation (i.e. batches and confounding factors) and to select the best predictors for modeling. Finally, a "stacking" ensemble learning technique is applied to build a robust classification model. Every step includes a checkpoint that the user may exploit to assess the effects of data management by looking at diagnostic plots, such as clustering and heatmaps, RLE boxplots, MDS or correlation plot.
    """

    bioc = "DaMiRseq"

    version("2.20.0", commit="a1dd1bc0e771460fa9ad387a47af3359210a4d11")
    version("2.14.0", commit="18c499a4a223e2105ff7fe9c25b097aed18f36f7")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-edaseq", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-sva", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-factominer", type=("build", "run"))
    depends_on("r-corrplot", type=("build", "run"))
    depends_on("r-randomforest", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-caret", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-lubridate", type=("build", "run"))
    depends_on("r-plsvarsel", type=("build", "run"))
    depends_on("r-kknn", type=("build", "run"))
    depends_on("r-fselector", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-ineq", type=("build", "run"))
    depends_on("r-arm", type=("build", "run"))
    depends_on("r-pls", type=("build", "run"))
    depends_on("r-rsnns", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))

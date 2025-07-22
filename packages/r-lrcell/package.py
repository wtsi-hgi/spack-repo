# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLrcell(RPackage):
    """Differential cell type change analysis using Logistic/linear Regression

    The goal of LRcell is to identify specific sub-cell types that drives the changes observed in a bulk RNA-seq differential gene expression experiment. To achieve this, LRcell utilizes sets of cell marker genes acquired from single-cell RNA-sequencing (scRNA-seq) as indicators for various cell types in the tissue of interest. Next, for each cell type, using its marker genes as indicators, we apply Logistic Regression on the complete set of genes with differential expression p-values to calculate a cell-type significance p-value. Finally, these p-values are compared to predict which one(s) are likely to be responsible for the differential gene expression pattern observed in the bulk RNA-seq experiments. LRcell is inspired by the LRpath[@sartor2009lrpath] algorithm developed by Sartor et al., originally designed for pathway/gene set enrichment analysis. LRcell contains three major components: LRcell analysis, plot generation and marker gene selection. All modules in this package are written in R. This package also provides marker genes in the Prefrontal Cortex (pFC) human brain region, human PBMC and nine mouse brain regions (Frontal Cortex, Cerebellum, Globus Pallidus, Hippocampus, Entopeduncular, Posterior Cortex, Striatum, Substantia Nigra and Thalamus).
    """

    bioc = "LRcell"

    version("1.16.0", commit="e6f72812c673f598c7f4514c469815acb3103631")
    version("1.10.0", commit="3cb2264cee3c59ee31156175610b4f5a584c95a7")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasics(RPackage):
	"""Bayesian Analysis of Single-Cell Sequencing data

	Single-cell mRNA sequencing can uncover novel cell-to-cell heterogeneity in gene expression levels in seemingly homogeneous populations of cells. However, these experiments are prone to high levels of technical noise, creating new challenges for identifying genes that show genuine heterogeneous expression within the population of cells under study. BASiCS (Bayesian Analysis of Single-Cell Sequencing data) is an integrated Bayesian hierarchical model to perform statistical analyses of single-cell RNA sequencing datasets in the context of supervised experiments (where the groups of cells of interest are known a priori, e.g. experimental conditions or cell types). BASiCS performs built-in data normalisation (global scaling) and technical noise quantification (based on spike-in genes). BASiCS provides an intuitive detection criterion for highly (or lowly) variable genes within a single group of cells. Additionally, BASiCS can compare gene expression patterns between two or more pre-specified groups of cells. Unlike traditional differential expression tools, BASiCS quantifies changes in expression that lie beyond comparisons of means, also allowing the study of changes in cell-to-cell heterogeneity. The latter can be quantified via a biological over-dispersion parameter that measures the excess of variability that is observed with respect to Poisson sampling noise, after normalisation and technical noise removal. Due to the strong mean/over-dispersion confounding that is typically observed for scRNA-seq datasets, BASiCS also tests for changes in residual over-dispersion, defined by residual values with respect to a global mean/over-dispersion trend.
	"""
	
	homepage = "https://github.com/catavallejos/BASiCS"
	bioc = "BASiCS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BASiCS_2.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BASiCS/BASiCS_2.14.0.tar.gz"]

    version("2.20.0", tag="RELEASE_3_21")
	version("2.14.0", sha256="88a911e7857c514dbebf8c2f45a2f6959ea9bb8804265e18bc5d87126c09c24d")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-matrix@1.5:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

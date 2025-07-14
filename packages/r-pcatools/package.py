# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcatools(RPackage):
	"""PCAtools: Everything Principal Components Analysis

	Principal Component Analysis (PCA) is a very powerful technique that has wide applicability in data science, bioinformatics, and further afield. It was initially developed to analyse large volumes of data in order to tease out the differences/relationships between the logical entities being analysed. It extracts the fundamental structure of the data without the need to build any model to represent it. This 'summary' of the data is arrived at through a process of reduction that can transform the large number of variables into a lesser number that are uncorrelated (i.e. the 'principal components'), while at the same time being capable of easy interpretation on the original data. PCAtools provides functions for data exploration via PCA, and allows the user to generate publication-ready figures. PCA is performed via BiocSingular - users can also identify optimal number of principal components via different metrics, such as elbow method and Horn's parallel analysis, which has relevance for data reduction in single-cell RNA-seq (scRNA-seq) and high dimensional mass cytometry data.
	"""
	
	homepage = "https://github.com/kevinblighe/PCAtools"
	bioc = "PCAtools"

	version("2.20.0", commit="c1da7440deb15cc9d4e9d8ad41aabeeafad25afa")
	version("2.14.0", commit="42f92cfde165e41babb3a88e1fc70225b767610b")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dqrng", type=("build", "run"))
	depends_on("r-beachmat", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))

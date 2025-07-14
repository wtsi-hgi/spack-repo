# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSponge(RPackage):
	"""Sparse Partial Correlations On Gene Expression

	This package provides methods to efficiently detect competitive endogeneous RNA interactions between two genes. Such interactions are mediated by one or several miRNAs such that both gene and miRNA expression data for a larger number of samples is needed as input. The SPONGE package now also includes spongEffects: ceRNA modules offer patient-specific insights into the miRNA regulatory landscape.
	"""
	
	bioc = "SPONGE" 

	version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", commit="c6d5f77f8e0fe3a220af7426b65fcb7dc6cea94a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ppcor", type=("build", "run"))
	depends_on("r-logging", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-grbase", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-cvms", type=("build", "run"))
	depends_on("r-mirbaseconverter", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tnet", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))

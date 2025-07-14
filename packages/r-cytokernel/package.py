# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytokernel(RPackage):
	"""Differential expression using kernel-based score test

	cytoKernel implements a kernel-based score test to identify differentially expressed features in high-dimensional biological experiments. This approach can be applied across many different high-dimensional biological data including gene expression data and dimensionally reduced cytometry-based marker expression data. In this R package, we implement functions that compute the feature-wise p values and their corresponding adjusted p values. Additionally, it also computes the feature-wise shrunk effect sizes and their corresponding shrunken effect size. Further, it calculates the percent of differentially expressed features and plots user-friendly heatmap of the top differentially expressed features on the rows and samples on the columns.
	"""
	
	bioc = "cytoKernel"

	version("1.14.0", commit="682ca5c53508a79c24b01ff2868339c1ef14b3d3")
	version("1.8.0", commit="7991fb26b8f8df44617d59c2982b57f704460234")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-ashr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

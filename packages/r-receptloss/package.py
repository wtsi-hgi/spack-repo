# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReceptloss(RPackage):
	"""Unsupervised Identification of Genes with Expression Loss in Subsets of Tumors

	receptLoss identifies genes whose expression is lost in subsets of tumors relative to normal tissue. It is particularly well-suited in cases where the number of normal tissue samples is small, as the distribution of gene expression in normal tissue samples is approximated by a Gaussian. Originally designed for identifying nuclear hormone receptor expression loss but can be applied transcriptome wide as well.
	"""
	
	bioc = "receptLoss"

	version("1.20.0", commit="9296b0aa4822e4ae2d599df789d54a2434ef4e9d")
	version("1.14.0", commit="1f5588dc635c432cc769e1c1e05b2388e0194ee4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

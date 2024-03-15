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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/receptLoss_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/receptLoss/receptLoss_1.14.0.tar.gz"]

	version("1.14.0", md5="3ccddd0181e8b78b843807d1378f86ef")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

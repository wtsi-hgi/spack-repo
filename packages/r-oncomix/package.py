# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROncomix(RPackage):
	"""Identifying Genes Overexpressed in Subsets of Tumors from Tumor-Normal mRNA Expression Data

	This package helps identify mRNAs that are overexpressed in subsets of tumors relative to normal tissue. Ideal inputs would be paired tumor-normal data from the same tissue from many patients (>15 pairs). This unsupervised approach relies on the observation that oncogenes are characteristically overexpressed in only a subset of tumors in the population, and may help identify oncogene candidates purely based on differences in mRNA expression between previously unknown subtypes.
	"""
	
	bioc = "oncomix" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/oncomix_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/oncomix/oncomix_1.24.0.tar.gz"]

	version("1.24.0", md5="dd6381604152d7cb96f7c592e8f82ab7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

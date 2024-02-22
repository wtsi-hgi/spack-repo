# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFabia(RPackage):
	"""FABIA: Factor Analysis for Bicluster Acquisition

	Biclustering by "Factor Analysis for Bicluster Acquisition" (FABIA). FABIA is a model-based technique for biclustering, that is clustering rows and columns simultaneously. Biclusters are found by factor analysis where both the factors and the loading matrix are sparse. FABIA is a multiplicative model that extracts linear dependencies between samples and feature patterns. It captures realistic non-Gaussian data distributions with heavy tails as observed in gene expression measurements. FABIA utilizes well understood model selection techniques like the EM algorithm and variational approaches and is embedded into a Bayesian framework. FABIA ranks biclusters according to their information content and separates spurious biclusters from true biclusters. The code is written in C.
	"""
	
	homepage = "http://www.bioinf.jku.at/software/fabia/fabia.html"
	bioc = "fabia" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/fabia_2.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/fabia/fabia_2.48.0.tar.gz"]

	version("2.48.0", md5="9d336b3c9a97aca0a6b062ec137f5566")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

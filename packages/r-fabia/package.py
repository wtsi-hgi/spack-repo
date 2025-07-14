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

	version("2.54.0", commit="14feaf1b2ca8f83bf831107fe3074d3fa1ab0caa")
	version("2.48.0", commit="162c211b363a3283667353d2614ecaf2db91f859")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

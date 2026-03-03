# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWcorr(RPackage):
	"""Weighted Correlations

	Calculates Pearson, Spearman, polychoric, and polyserial correlation coefficients, in weighted or unweighted form. The package implements tetrachoric correlation as a special case of the polychoric and biserial correlation as a specific case of the polyserial.
	"""
	
	homepage = "https://american-institutes-for-research.github.io/wCorr/"
	cran = "wCorr" 

	version("1.9.8", md5="947633dbdd3547f0b4b6d7d54473d482")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

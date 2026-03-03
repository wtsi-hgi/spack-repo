# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeights(RPackage):
	"""Weighting and Weighted Statistics

	Provides a variety of functions for producing simple weighted statistics, such as weighted Pearson's correlations, partial correlations, Chi-Squared statistics, histograms, and t-tests.  Also now includes some software for quickly recoding survey data and plotting estimates from interaction terms in regressions (and multiply imputed regressions) both with and without weights. NOTE: Weighted partial correlation calculations pulled to address a bug.
	"""
	
	cran = "weights" 

	version("1.0.4", md5="ca34db0e393f2b0f15a8bfcb89ee01b8")

	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))

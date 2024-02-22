# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpvam(RPackage):
	"""Maximum Likelihood Estimation of Multiple Membership Mixed
Models Used in Value-Added Modeling

	An EM algorithm, Karl et al. (2013) <doi:10.1016/j.csda.2012.10.004>, is used to estimate the generalized, variable, and complete persistence models, Mariano et al. (2010) <doi:10.3102/1076998609346967>. These are multiple-membership linear mixed models with teachers modeled as "G-side" effects and students modeled with either "G-side" or "R-side" effects.
	"""
	
	cran = "GPvam" 

	version("3.0-9", md5="bdbaec9683726d1587821f221028862d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

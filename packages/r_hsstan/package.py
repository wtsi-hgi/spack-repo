# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHsstan(RPackage):
	"""Hierarchical Shrinkage Stan Models for Biomarker Selection

	Linear and logistic regression models penalized with hierarchical
  shrinkage priors for selection of biomarkers (or more general variable
  selection), which can be fitted using Stan (Carpenter et al. (2017)
  <doi:10.18637/jss.v076.i01>). It implements the horseshoe and regularized
  horseshoe priors (Piironen and Vehtari (2017) <doi:10.1214/17-EJS1337SI>),
  as well as the projection predictive selection approach to recover a sparse
  set of predictive biomarkers (Piironen, Paasiniemi and Vehtari (2020)
  <doi:10.1214/20-EJS1711>).
	"""
	
	homepage = "https://github.com/mcol/hsstan"
	cran = "hsstan" 

	version("0.8.2", md5="45f800811068b7462e4208d61314e7f5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-loo@2.1:", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-rcpp@0.12.15:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-bh@1.66.0.1:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.4:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))

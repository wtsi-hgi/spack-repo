# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetafuse(RPackage):
	"""Fused Lasso Approach in Regression Coefficient Clustering

	Fused lasso method to cluster and estimate regression coefficients
    of the same covariate across different data sets when a large number of
    independent data sets are combined. Package supports Gaussian, binomial,
    Poisson and Cox PH models.
	"""
	
	cran = "metafuse" 

	version("2.0-1", md5="ae72588b77f37abfcc00cd39f6cced77")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))

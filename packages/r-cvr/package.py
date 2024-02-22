# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvr(RPackage):
	"""Canonical Variate Regression

	Perform canonical variate regression (CVR) for two sets of covariates and a univariate
            response, with regularization and weight parameters tuned by cross validation.  
	"""
	
	cran = "CVR" 

	version("0.1.1", md5="c62f0d205655667da3c26cc9bacb8458")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-pma", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

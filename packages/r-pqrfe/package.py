# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPqrfe(RPackage):
	"""Penalized Quantile Regression with Fixed Effects

	Quantile regression with fixed effects is a general model for longitudinal data. Here we proposed to solve it by several methods. The estimation methods include three loss functions as check, asymmetric least square and asymmetric Huber functions; and three structures as simple regression, fixed effects and fixed effects with penalized intercepts by LASSO.    
	"""
	
	cran = "pqrfe" 

	version("1.1", md5="ea08b7bbdd8a5020c3048f4cfbd4e5ea")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass@7.3.49:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

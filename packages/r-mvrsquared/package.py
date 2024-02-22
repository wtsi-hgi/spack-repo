# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvrsquared(RPackage):
	"""Compute the Coefficient of Determination for Vector or Matrix
Outcomes

	Compute the coefficient of determination for outcomes in n-dimensions. 
  May be useful for multidimensional predictions (such as a multinomial model) or
  calculating goodness of fit from latent variable models such as probabilistic
  topic models like latent Dirichlet allocation or deterministic topic models 
  like latent semantic analysis. Based on Jones (2019) <arXiv:1911.11061>.
	"""
	
	homepage = "https://github.com/TommyJones/mvrsquared"
	cran = "mvrsquared" 

	version("0.1.5", md5="b63111f2104bc6edab37fb0dddedc6ba")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppthread@2.1.3:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGas(RPackage):
	"""Generalized Autoregressive Score Models

	Simulate, estimate and forecast using univariate and multivariate GAS models 
  as described in Ardia et al. (2019) <doi:10.18637/jss.v088.i06>.
	"""
	
	homepage = "https://github.com/LeopoldoCatania/GAS"
	cran = "GAS" 

	version("0.3.4", md5="81c59f348df22c811ce9930be709b957")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

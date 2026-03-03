# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBark(RPackage):
	"""Bayesian Additive Regression Kernels

	Bayesian Additive Regression Kernels (BARK) provides
	an implementation for non-parametric function estimation using Levy
	Random Field priors for functions that may be represented as a
	sum of additive multivariate kernels.  Kernels are located at
	every data point as in Support Vector Machines, however, coefficients 
	may be heavily shrunk to zero under the Cauchy process prior, or even, 
	set to zero.  The number of active features is controlled by priors on
	precision parameters within the kernels, permitting feature selection. For 
	more details see Ouyang, Z (2008) "Bayesian Additive Regression Kernels",
	Duke University. PhD dissertation, Chapter 3 and Wolpert, R. L, Clyde, M.A, 
	and Tu, C. (2011) "Stochastic Expansions with Continuous Dictionaries Levy
	Adaptive Regression Kernels, Annals of Statistics Vol (39) pages 1916-1962 
	<doi:10.1214/11-AOS889>.
	"""
	
	homepage = "https://www.R-project.org"
	cran = "bark" 

	version("1.0.4", md5="4a7e5bfc4096b922ada0850bc4cda0ac")


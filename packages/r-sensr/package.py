# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensr(RPackage):
	"""Thurstonian Models for Sensory Discrimination

	Provides methods for sensory discrimination methods;
  duotrio, tetrad, triangle, 2-AFC, 3-AFC, A-not A, same-different,
  2-AC and degree-of-difference.
  This enables the calculation of d-primes, standard errors of
  d-primes, sample size and power computations, and
  comparisons of different d-primes. Methods for profile likelihood
  confidence intervals and plotting are included. Most methods are 
  described in Brockhoff, P.B. and Christensen, R.H.B. (2010) 
  <doi:10.1016/j.foodqual.2009.04.003>. 
	"""
	
	homepage = "https://github.com/aigorahub/sensR"
	cran = "sensR" 

	version("1.5-3", md5="25f66f67a8e87622d9ea9ff3e77fbc21")

	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))

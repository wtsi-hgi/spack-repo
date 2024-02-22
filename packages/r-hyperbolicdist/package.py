# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHyperbolicdist(RPackage):
	"""The Hyperbolic Distribution

	Maintenance has been discontinued for this package. It has been
	     superseded by 'GeneralizedHyperbolic'. 'GeneralizedHyperbolic' 
	     includes all the functionality of 'HyperbolicDist' and more 
	     and is based on a more rational design. 'HyperbolicDist' 
	     provides functions for the hyperbolic and related 
	     distributions. Density, distribution and quantile functions 
	     and random number generation are provided for the hyperbolic 
	     distribution, the generalized hyperbolic distribution, 
	     the generalized inverse Gaussian distribution and the 
	     skew-Laplace distribution. Additional functionality is 
	     provided for the hyperbolic distribution, including 
	     fitting of the hyperbolic to data.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "HyperbolicDist" 

	version("0.6-5", md5="cd6dd2ea93303c2803e7348cad3a3995")

	depends_on("r@3.5:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLognorm(RPackage):
	"""Functions for the Lognormal Distribution

	The lognormal distribution  
  (Limpert et al. (2001) <doi:10.1641/0006-3568(2001)051%5B0341:lndats%5D2.0.co;2>)
  can characterize uncertainty that is bounded by zero.
  This package provides estimation of distribution parameters, computation of
  moments and other basic statistics, and an approximation of the distribution
  of the sum of several correlated lognormally distributed variables 
  (Lo 2013 <doi:10.12988/ams.2013.39511>) and the approximation of the 
  difference of two correlated lognormally distributed variables
  (Lo 2012 <doi:10.1155/2012/838397>).
	"""
	
	homepage = "https://github.com/bgctw/lognorm"
	cran = "lognorm" 

	version("0.1.10", md5="14a1f39ee82351caec0dde38dd952885")

	depends_on("r-matrix", type=("build", "run"))

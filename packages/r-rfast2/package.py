# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RRfast2(RPackage):
	"""A Collection of Efficient and Extremely Fast R Functions II

	A collection of fast statistical and utility functions for data analysis. Functions for regression, maximum likelihood, column-wise statistics and many more have been included. C++ has been utilized to speed up the functions.
	"""
	
	homepage = "https://github.com/RfastOfficial/Rfast2"
	cran = "Rfast2" 

	version("0.1.5.1", md5="016c2d1b5eef2c83acd25d4cf2c3c0c8")

	depends_on("r@3.5.0:", type=("build", "run"))
	depends_on("r-rcpp@0.12.3:", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rcpp@0.12.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))


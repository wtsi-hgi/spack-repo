# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovatest(RPackage):
	"""Tests on Properties of Space-Time Covariance Functions

	Tests on properties of space-time covariance functions.
    Tests on symmetry, separability and for assessing 
    different forms of non-separability are available. Moreover tests on 
    some classes of covariance functions, such that the classes of 
    product-sum models, Gneiting models and integrated product models have 
    been provided.  It is the companion R package to the papers of  
    Cappello, C., De Iaco, S., Posa, D., 2018, Testing the type of non-separability 
    and some classes of space-time covariance function models <doi:10.1007/s00477-017-1472-2>
    and Cappello, C., De Iaco, S., Posa, D., 2020, covatest: an R package for
    selecting a class of space-time covariance functions <doi:10.18637/jss.v094.i01>.
	"""
	
	cran = "covatest" 

	version("1.2.3", md5="eef70a912e02b791e7db5900159da8d2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-sp@0.9.72:", type=("build", "run"))
	depends_on("r-spacetime@1.0.0:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoodist(RPackage):
	"""Some Distributions from the 'Boost' Library and More

	Make some distributions from the 'C++' library 'Boost'
    available in 'R'. In addition, the normal-inverse Gaussian distribution
    and the generalized inverse Gaussian distribution are provided. The 
    distributions are represented by 'R6' classes. The method to sample from 
    the generalized inverse Gaussian distribution is the one given in 
    "Random variate generation for the generalized inverse Gaussian 
    distribution" Luc Devroye (2012) <doi:10.1007/s11222-012-9367-z>.
	"""
	
	homepage = "https://github.com/stla/boodist"
	cran = "boodist" 

	version("1.0.0", md5="37ac7d61f7eb07e870e2b84944026d97")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

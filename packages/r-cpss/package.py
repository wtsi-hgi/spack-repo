# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpss(RPackage):
	"""Change-Point Detection by Sample-Splitting Methods

	Implements multiple change searching algorithms for a variety of 
    frequently considered parametric change-point models. In particular, it 
    integrates a criterion proposed by Zou, Wang and Li (2020) 
    <doi:10.1214/19-AOS1814> to select the number of change-points in a 
    data-driven fashion. Moreover, it also provides interfaces for 
    user-customized change-point models with one's own cost function and 
    parameter estimation routine. It is easy to get started with the 
    cpss.* set of functions by accessing their documentation pages 
    (e.g., ?cpss).
	"""
	
	homepage = "https://github.com/ghwang-nk/cpss"
	cran = "cpss" 

	version("0.0.3", md5="28836dbae254225a088289193c696efb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

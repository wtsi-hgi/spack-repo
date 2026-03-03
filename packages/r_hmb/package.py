# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmb(RPackage):
	"""Hierarchical Model-Based Estimation Approach

	For estimation of a variable of interest using two sources of auxiliary information available in a nested structure. For reference see Saarela et al. (2016)<doi:10.1007/s13595-016-0590-1> and Saarela et al. (2018) <doi:10.3390/rs10111832>. 
	"""
	
	cran = "HMB" 

	version("1.1", md5="762b3c999dac5946dc128b8f3c94a393")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

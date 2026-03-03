# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetutils(RPackage):
	"""A Collection of Tools for Network Analysis

	Provides a collection of network analytic (convenience) functions which are missing in other standard packages. This includes triad census with attributes <doi:10.1016/j.socnet.2019.04.003>, core-periphery models <doi:10.1016/S0378-8733(99)00019-2>, and several graph generators. Most functions are build upon 'igraph'.  
	"""
	
	homepage = "https://github.com/schochastics/netUtils/"
	cran = "netUtils" 

	version("0.8.2", md5="4860500a2dd15111f7208d38b35c3047")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

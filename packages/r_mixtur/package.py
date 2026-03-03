# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixtur(RPackage):
	"""Modelling Continuous Report Visual Short-Term Memory Studies

	A set of utility functions for analysing and modelling data from 
    continuous report short-term memory experiments using either the 2-component
    mixture model of Zhang and Luck (2008) <doi:10.1038/nature06860> or the 
    3-component mixture model of Bays et al. (2009) <doi:10.1167/9.10.7>. Users 
    are also able to simulate from these models.
	"""
	
	homepage = "https://github.com/JimGrange/mixtur"
	cran = "mixtur" 

	version("1.2.1", md5="49f40fb4732e9e6c73e4d3b9241797b6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))

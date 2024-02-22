# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistrr(RPackage):
	"""Estimate and Manage Empirical Distributions

	Tools to estimate and manage empirical distributions,
    which should work with survey data. One of the main features is the 
    possibility to create data cubes of estimated statistics, that include
    all the combinations of the variables of interest (see for example functions
    dcc5() and dcc6()).
	"""
	
	homepage = "https://gibonet.github.io/distrr"
	cran = "distrr" 

	version("0.0.6", md5="887578f258cde49cd4e36bc20766b7e2")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr@0.7:", type=("build", "run"))

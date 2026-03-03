# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWacs(RPackage):
	"""Multivariate Weather-State Approach Conditionally Skew-Normal
Generator

	A multivariate weather generator for daily climate variables based 
    on weather-states (Flecher et al. (2010) <doi:10.1029/2009WR008098>). 
    It uses a Markov chain for modeling the succession of weather states. 
    Conditionally to the weather states, the multivariate variables are modeled using the family 
    of Complete Skew-Normal distributions. Parameters are estimated on measured series. Must 
    include the variable 'Rain' and can accept as many other variables as desired.
	"""
	
	homepage = "https://miat.inrae.fr/site/Ronan_TREPOS"
	cran = "WACS" 

	version("1.1.0", md5="0305c1fdc406f4f6610da496db149df0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntmed(RPackage):
	"""Mediation Analysis using Interventional Effects

	Implementing the interventional effects for mediation analysis for up to 3 mediators.
    The methods used are based on VanderWeele, Vansteelandt and Robins (2014) <doi:10.1097/ede.0000000000000034>, 
    Vansteelandt and Daniel (2017) <doi:10.1097/ede.0000000000000596> and Chan and Leung (2020; unpublished manuscript, available on request from the author of this package).
    Linear regression, logistic regression and Poisson regression are used for continuous, binary 
    and count mediator/outcome variables respectively.
	"""
	
	cran = "intmed" 

	version("0.1.2", md5="d495194ee54c5ba7613c68118e58117e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))

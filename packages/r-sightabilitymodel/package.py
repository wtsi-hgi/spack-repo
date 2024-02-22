# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSightabilitymodel(RPackage):
	"""Wildlife Sightability Modeling

	Uses logistic regression to model the probability of detection as a function of covariates. 
             This model is then used with observational survey data to estimate population size, while
             accounting for uncertain detection.  See Steinhorst and Samuel (1989).
	"""
	
	homepage = "https://github.com/jfieberg/SightabilityModel"
	cran = "SightabilityModel" 

	version("1.5.5", md5="33a9b126af7ddb015df3d18157d3cd65")

	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))

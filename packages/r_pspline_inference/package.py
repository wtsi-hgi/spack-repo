# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsplineInference(RPackage):
	"""Estimation of Characteristics of Seasonal and Sporadic
Infectious Disease Outbreaks Using Generalized Additive
Modeling with Penalized Basis Splines

	Inference of infectious disease outcomes using generalized additive
    (mixed) models with penalized basis splines (P-Splines). See 
    <https://medrxiv.org/cgi/content/short/2020.07.14.20138180v1>.
	"""
	
	homepage = "https://github.com/weinbergerlab/pspline.inference"
	cran = "pspline.inference" 

	version("1.0.4", md5="881e257329881e26387aa08dc979928a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))

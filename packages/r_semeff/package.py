# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemeff(RPackage):
	"""Automatic Calculation of Effects for Piecewise Structural
Equation Models

	Automatically calculate direct, indirect, and total effects for 
    piecewise structural equation models, comprising lists of fitted models 
    representing structured equations (Lefcheck, 2016 <doi:10/f8s8rb>). 
    Confidence intervals are provided via bootstrapping.
	"""
	
	homepage = "https://murphymv.github.io/semEff/"
	cran = "semEff" 

	version("0.6.1", md5="6f7b0d9e5b7b9907d4e85a48c72851a8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))

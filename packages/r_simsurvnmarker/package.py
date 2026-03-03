# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimsurvnmarker(RPackage):
	"""Simulate Survival Time and Markers

	Provides functions to simulate from joint survival and marker 
    models. The user can specific all basis functions of time, random or 
    deterministic covariates, random or deterministic left-truncation and 
    right-censoring times, and model parameters.
	"""
	
	homepage = "https://github.com/boennecd/SimSurvNMarker"
	cran = "SimSurvNMarker" 

	version("0.1.3", md5="9c2955059306e8334dae3ea47d0b85e9")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

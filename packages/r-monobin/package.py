# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonobin(RPackage):
	"""Monotonic Binning for Credit Rating Models

	Performs monotonic binning of numeric risk factor in credit rating models (PD, LGD, EAD) 
	development. All functions handle both binary and continuous target variable. 
	Functions that use isotonic regression in the first stage of binning process have an additional 
	feature for correction of minimum percentage of observations and minimum target rate per bin. 	
	Additionally, monotonic trend can be identified based on raw data or, if known in advance,
	forced by functions' argument. Missing values and other possible special values are treated 
	separately from so-called complete cases.
	"""
	
	homepage = "https://github.com/andrija-djurovic/monobin"
	cran = "monobin" 

	version("0.2.4", md5="adc0bb912d4b92231c29aca690919c7e")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))

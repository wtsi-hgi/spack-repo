# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLtrctrees(RPackage):
	"""Survival Trees to Fit Left-Truncated and Right-Censored and
Interval-Censored Survival Data

	Recursive partition algorithms designed for fitting survival tree with left-truncated and right censored (LTRC) data, as well as interval-censored data.
    The LTRC trees can also be used to fit survival tree with time-varying covariates.
	"""
	
	cran = "LTRCtrees" 

	version("1.1.1", md5="dfe0c0a27eb3a50b0731b2e5817560d4")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-partykit@1.2:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-inum", type=("build", "run"))
	depends_on("r-icenreg", type=("build", "run"))
	depends_on("r-icens", type=("build", "run"))
	depends_on("r-interval", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeightquant(RPackage):
	"""Weights for Incomplete Longitudinal Data and Quantile Regression

	Estimation of observation-specific weights for incomplete longitudinal data and bootstrap procedure for weighted quantile regressions. See Jacqmin-Gadda, Rouanet, Mba, Philipps, Dartigues (2020) for details <doi:10.1177/0962280220909986>.
	"""
	
	cran = "weightQuant" 

	version("1.0.1", md5="af838867a9c68d817e112083525734c6")

	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

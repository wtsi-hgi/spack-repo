# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWce(RPackage):
	"""Weighted Cumulative Exposure Models

	A flexible method for modeling cumulative effects of time-varying exposures, weighted according to their relative proximity in time, and represented by time-dependent covariates. The current implementation estimates the weight function in the Cox proportional hazards model. The function that assigns weights to doses taken in the past is estimated using cubic regression splines.
	"""
	
	cran = "WCE" 

	version("1.0.3", md5="3f9c277c96ca2b574fd622194bde2917")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))

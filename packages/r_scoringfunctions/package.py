# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScoringfunctions(RPackage):
	"""A Collection of Scoring Functions for Assessing Point Forecasts

	
    Implements multiple consistent scoring functions
    (Gneiting T (2011) <doi:10.1198/jasa.2011.r10138>) for assessing point
    forecasts and point predictions. Detailed documentation of scoring
    functions' properties is included for facilitating interpretation of
    results.
	"""
	
	cran = "scoringfunctions" 

	version("0.0.6", md5="de3c7035d2a36d31d905514e6508d813")

	depends_on("r@4:", type=("build", "run"))

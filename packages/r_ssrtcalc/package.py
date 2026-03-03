# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsrtcalc(RPackage):
	"""Easy SSRT Calculation

	This is a collection of functions to calculate stop-signal reaction time (SSRT). Includes functions for both "integration" and "mean" methods; both fixed and adaptive stop-signal delays are supported (see appropriate functions). Calculation is based on Verbruggen et al. (2019) <doi:10.7554/eLife.46323.001> and Verbruggen et al. (2013) <doi:10.1177/0956797612457390>. 
	"""
	
	cran = "SSRTcalc" 

	version("0.3.3", md5="b0ea929b62dc62fc701df96c8f30f34e")

	depends_on("r@3.5:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REventtrack(RPackage):
	"""Event Prediction for Time-to-Event Endpoints

	Implements the hybrid framework for event prediction described in Fang & Zheng (2011, <doi:10.1016/j.cct.2011.05.013>). To estimate the survival function the event prediction is based on, a piecewise exponential hazard function is fit to the time-to-event data to infer the potential change points. Prior to the last identified change point, the survival function is estimated using Kaplan-Meier, and the tail after the change point is fit using piecewise exponential. 
	"""
	
	cran = "eventTrack" 

	version("1.0.3", md5="678a2367632e4834933aad8382da9516")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-muhaz", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))

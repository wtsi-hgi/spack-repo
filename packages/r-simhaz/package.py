# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimhaz(RPackage):
	"""Simulated Survival and Hazard Analysis for Time-Dependent
Exposure

	Generate power for the Cox proportional hazards model by simulating survival events data with time dependent exposure status for subjects. A dichotomous exposure variable is considered with a single transition from unexposed to exposed status during the subject's time on study.
	"""
	
	homepage = "http://www.stat.berkeley.edu/~rabbee/research_webpage.htm"
	cran = "SimHaz" 

	version("0.1", md5="9010fbcc5c359feb8aeb15a5e61e8328")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))

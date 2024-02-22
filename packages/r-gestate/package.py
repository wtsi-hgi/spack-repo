# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGestate(RPackage):
	"""Generalised Survival Trial Assessment Tool Environment

	Provides tools to assist planning and monitoring of time-to-event trials under complicated censoring assumptions and/or non-proportional hazards. There are three main components: The first is analytic calculation of predicted time-to-event trial properties, providing estimates of expected hazard ratio, event numbers and power under different analysis methods. The second is simulation, allowing stochastic estimation of these same properties. Thirdly, it provides parametric event prediction using blinded trial data, including creation of prediction intervals. Methods are based upon numerical integration and a flexible object-orientated structure for defining event, censoring and recruitment distributions (Curves).
	"""
	
	cran = "gestate" 

	version("1.6.0", md5="faad044e1bea165edf670d0db28ed1c4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))

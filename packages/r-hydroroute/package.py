# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydroroute(RPackage):
	"""Trace Longitudinal Hydropeaking Waves

	Implements an empirical approach referred to as PeakTrace which uses multiple hydrographs to detect and follow hydropower plant-specific hydropeaking waves at the sub-catchment scale and to describe how hydropeaking flow parameters change along the longitudinal flow path. The method is based on the identification of associated events and uses (linear) regression models to describe translation and retention processes between neighboring hydrographs. Several regression model results are combined to arrive at a power plant-specific model. The approach is proposed and validated in Greimel et al. (2022) <doi:10.1002/rra.3978>. The identification of associated events is based on the event detection implemented in 'hydropeak'.
	"""
	
	cran = "hydroroute" 

	version("0.1.2", md5="0e506269d5c258dd01bdf6ca8cb6855a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggpmisc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-hydropeak", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))

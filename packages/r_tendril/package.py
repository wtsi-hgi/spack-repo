# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTendril(RPackage):
	"""Compute and Display Tendril Plots

	Compute the coordinates to produce a tendril plot. 
    In the tendril plot, each tendril (branch) represents a type of events, 
    and the direction of the tendril is dictated by on which treatment arm the 
    event is occurring. If an event is occurring on the first of the two 
    specified treatment arms, the tendril bends in a clockwise direction. 
    If an event is occurring on the second of the treatment arms, the
    tendril bends in an anti-clockwise direction. 
    Ref: Karpefors, M and Weatherall, J., "The Tendril Plot - a novel visual summary 
    of the incidence, significance and temporal aspects of adverse events in 
    clinical trials" - JAMIA 2018; 25(8): 1069-1073 <doi:10.1093/jamia/ocy016>.
	"""
	
	homepage = "https://github.com/Karpefors/Tendril"
	cran = "Tendril" 

	version("2.0.4", md5="567af458ac8bfdddc31af97a035c57a8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))

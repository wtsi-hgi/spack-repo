# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydropeak(RPackage):
	"""Detect and Characterize Sub-Daily Flow Fluctuations

	An important environmental impact on running water ecosystems 
    is caused by hydropeaking - the discontinuous release of turbine water 
    because of peaks of energy demand. An event-based algorithm is implemented 
    to detect flow fluctuations referring to increase events (IC) and decrease 
    events (DC). For each event, a set of parameters related to the fluctuation 
    intensity is calculated. The framework is introduced in Greimel et al. (2016) 
    "A method to detect and characterize sub-daily flow fluctuations" 
    <doi:10.1002/hyp.10773> and can be used to identify different fluctuation 
    types according to the potential source: e.g., sub-daily flow fluctuations 
    caused by hydropeaking, rainfall, or snow and glacier melt.
    This is a companion to the package 'hydroroute', which is used to detect and 
    follow hydropower plant-specific hydropeaking waves at the sub-catchment 
    scale and to describe how hydropeaking flow parameters change along the
    longitudinal flow path as proposed and validated in Greimel et al. (2022).
	"""
	
	cran = "hydropeak" 

	version("0.1.2", md5="67611da582c573c7c2f00e4b5d5ff3c5")

	depends_on("r@4.1:", type=("build", "run"))

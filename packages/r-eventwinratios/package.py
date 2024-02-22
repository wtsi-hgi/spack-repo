# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REventwinratios(RPackage):
	"""Event-Specific Win Ratios for Terminal and Non-Terminal Events

	Provides several confidence interval and testing procedures using
    event-specific win ratios for semi-competing risks data with non-terminal
    and terminal events, as developed in Yang et al. (2021<doi:10.1002/sim.9266>). 
    Compared with conventional methods for survival data, these procedures are 
    designed to utilize more data for improved inference procedures with 
    semi-competing risks data. The event-specific win ratios were introduced in 
    Yang and Troendle (2021<doi:10.1177/1740774520972408>). In this package, 
    the event-specific win ratios and confidence intervals are obtained for each 
    event type, and several testing procedures are developed for the global null 
    of no treatment effect on either terminal or non-terminal events. Furthermore,
    a test of proportional hazard assumptions, under which the event-specific win 
    ratios converge to the hazard ratios, and a test of equal hazard ratios are 
    provided. For summarizing the treatment effect on all events, confidence 
    intervals for linear combinations of the event-specific win ratios are available
    using pre-determined or data-driven weights. Asymptotic properties of these 
    inference procedures are discussed in Yang et al (2021<doi:10.1002/sim.9266>). 
    Also, transformations are used to yield better control of the type one error 
    rates for moderately sized data sets.
	"""
	
	cran = "EventWinRatios" 

	version("1.0.0", md5="fadba59d53192aa719fff9816ac9b874")


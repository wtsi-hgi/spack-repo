# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAoristic(RPackage):
	"""Generates Aoristic Probability Distributions

	It can sometimes be difficult to ascertain when some events (such as property crime)
    occur because the victim is not present when the crime happens. As a result, police databases often
    record a 'start' (or 'from') date and time, and an 'end' (or 'to') date and time. The time span between
    these date/times can be minutes, hours, or sometimes days, hence the term 'Aoristic'. 
    Aoristic is one of the past tenses in Greek and represents an uncertain occurrence in time. 
    For events with a location describes with either a latitude/longitude, or X,Y coordinate pair, 
    and a start and end date/time, this package generates an aoristic data frame with aoristic weighted
    probability values for each hour of the week, for each observation. The coordinates are not 
    necessary for the program to calculate aoristic weights; however, they are part of this package 
    because a spatial component has been integral to aoristic analysis from the start. Dummy 
    coordinates can be introduced if the user only has temporal data. Outputs include an aoristic 
    data frame, as well as summary graphs and displays.   
        For more information see:
    Ratcliffe, JH (2002) Aoristic signatures and the temporal analysis of high volume crime patterns, 
    Journal of Quantitative Criminology. 18 (1): 23-43.
    Note: This package replaces an original 'aoristic' package (version 0.6) by George Kikuchi that 
    has been discontinued with his permission. 
	"""
	
	cran = "aoristic" 

	version("1.1.1", md5="e759007069fa79e79bc8c4f920561465")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))

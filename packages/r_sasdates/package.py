# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSasdates(RPackage):
	"""Convert the Dates to 'SAS' Formats

	Converts the dates to different 'SAS' date formats. In 'SAS' dates are a special case of 
             numeric values. Each day is assigned a specific numeric value, starting from January 1, 1960.
             This date is assigned the date value 0, and the next date has a date value of 1 and so on.
             The previous days to this date are represented by -1 , -2 and so on. With this approach, 
             'SAS' can represent any date in the future or any date in the past. There are many date 
             formats used in 'SAS' to represent date-time. Here, we try to develop functions which will
             convert the date to different 'SAS' date formats.
	"""
	
	cran = "SASdates" 

	version("0.1.0", md5="d3e0a17430119627f822ce81373e140b")


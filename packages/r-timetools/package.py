# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimetools(RPackage):
	"""Seasonal/Sequential (Instants/Durations, Even or not) Time
Series

	Objects to manipulate sequential and seasonal time series. Sequential time series based on time instants and time durations are handled. Both can be regularly or unevenly spaced (overlapping durations are allowed). Only POSIX* format are used for dates and times. The following classes are provided : 'POSIXcti', 'POSIXctp', 'TimeIntervalDataFrame', 'TimeInstantDataFrame', 'SubtimeDataFrame' ; methods to switch from a class to another and to modify the time support of series (hourly time series to daily time series for instance) are also defined. Tools provided can be used for instance to handle environmental monitoring data (not always produced on a regular time base).
	"""
	
	homepage = "https://sourceforge.net/projects/timetools/"
	cran = "timetools" 

	version("1.15.3", md5="528bd0d05bc415afb786b24dfedba69a")


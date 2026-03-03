# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhysactbedrest(RPackage):
	"""Marks Periods of 'Bedrest' in Actigraph Accelerometer Data

	Contains a function to categorize accelerometer readings collected in free-living (e.g., for 24 hours/day for 7 days), preprocessed and compressed as counts (unit-less value) in a specified time period termed epoch (e.g., 1 minute) as either bedrest (sleep) or active.  The input is a matrix with a timestamp column and a column with number of counts per epoch. The output is the same dataframe with an additional column termed bedrest. In the bedrest column each line (epoch) contains a function-generated classification 'br' or 'a' denoting bedrest/sleep and activity, respectively.  The package is designed to be used after wear/nonwear marking function in the 'PhysicalActivity' package.  Version 1.1 adds preschool thresholds and corrects for possible errors in algorithm implementation.    
	"""
	
	cran = "PhysActBedRest" 

	version("1.1", md5="491d4ee14acc56ae648badd58eef9af2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))

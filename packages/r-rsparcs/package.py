# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsparcs(RPackage):
	"""Sites, Population, and Records Cleaning Skills

	Data cleaning including 1) generating datasets for time-series and case-crossover analyses based on raw hospital records, 2) linking individuals to an areal map, 3) picking out cases living within a buffer of certain size surrounding a site, etc. For more information, please refer to Zhang W,etc. (2018) <doi:10.1016/j.envpol.2018.08.030>. 
	"""
	
	cran = "rSPARCS" 

	version("0.1.1", md5="018ed50d97ce95acbbb555f811ca625e")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-tigris", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))

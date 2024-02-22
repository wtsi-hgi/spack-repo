# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCruts(RPackage):
	"""Interface to Climatic Research Unit Time-Series Version 3.21
Data

	Functions for reading in and manipulating CRU TS3.21: Climatic
    Research Unit (CRU) Time-Series (TS) Version 3.21 data.
	"""
	
	cran = "cruts" 

	version("1.1", md5="59514afa84995ab406477d2853a0e308")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))

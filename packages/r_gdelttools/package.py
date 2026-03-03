# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdelttools(RPackage):
	"""Download, Slice, and Normalize GDELT V1 Event and Sentiment API
Data

	The GDELT V1 Event data set is over 41 GB now and growing 250 MB 
    a month. The number of source articles has increased over time and unevenly 
    across countries. This package makes it easy to download a subset of that 
    data, then normalize that data to facilitate valid time series analysis.
	"""
	
	cran = "GDELTtools" 

	version("1.7", md5="96d5ce5ff0c5fb82f9945fb6d9325489")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-datetimeutils", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWearables(RPackage):
	"""Tools to Read and Convert Wearables Data

	
    Package to read Empatica E4 data, perform several transformations, perform signal
    processing and analyses, including batch analyses.
	"""
	
	cran = "wearables" 

	version("0.8.1", md5="dee1c8482f787f14e06dbf3965396292")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rhrv", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-waveslim", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-padr", type=("build", "run"))
	depends_on("r-varian", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))

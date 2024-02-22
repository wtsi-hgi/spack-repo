# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpolygrowth(RPackage):
	"""Individual Growth Curve Parameter Calculation using Polynomial
Functions

	Calculation of key bacterial growth curve parameters using fourth degree polynomial functions. 
    Six growth curve parameters are provided including peak growth rate, doubling time, lag time, maximum growth, and etc.
    'ipolygrowth' takes time series data from individual biological samples (with technical replicates) or multiple samples.
	"""
	
	homepage = "https://github.com/kivanvan/ipolygrowth"
	cran = "ipolygrowth" 

	version("0.1.2", md5="5c105b2c5231152ef167121fa40e40ad")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPadr(RPackage):
	"""Quickly Get Datetime Data Ready for Analysis

	Transforms datetime data into a format ready for analysis.
    It offers two core functionalities; aggregating data to a higher level interval
    (thicken) and imputing records where observations were absent (pad). 
	"""
	
	homepage = "https://github.com/EdwinTh/padr"
	cran = "padr" 

	version("0.6.2", md5="8b3f1987f0c2bddf67ec95125281a891")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))

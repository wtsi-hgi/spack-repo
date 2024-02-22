# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCombinedevents(RPackage):
	"""Calculate Scores and Marks for Track and Field Combined Events

	Includes functions to calculate scores and marks for track and
    field combined events competitions. The functions are based on the scoring
    tables for combined events set forth by the International Association of 
    Athletics Federation (2001).
	"""
	
	homepage = "https://katie-frank.github.io/combinedevents/"
	cran = "combinedevents" 

	version("0.1.1", md5="a7f6272b59e443175763824019d33f3b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

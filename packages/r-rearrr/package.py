# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRearrr(RPackage):
	"""Rearranging Data

	Arrange data by a set of methods. Use rearrangers to reorder
    data points and mutators to change their values. From basic utilities,
    to centering the greatest value, to swirling in 3-dimensional space,
    'rearrr' enables creativity when plotting and experimenting with data.
	"""
	
	homepage = "https://github.com/ludvigolsen/rearrr"
	cran = "rearrr" 

	version("0.3.4", md5="74335f73a736d52e6c044f76d547a66f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))

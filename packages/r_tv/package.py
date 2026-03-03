# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTv(RPackage):
	"""Tools for Creating Time-Varying Datasets

	Create a time-varying dataset using features, exposure, and
    look back specifications.
	"""
	
	cran = "tv" 

	version("2.0.2", md5="1cb2c6799bc8b719b6f8ca8dc560a377")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr@1.1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))

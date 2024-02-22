# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrclimr(RPackage):
	"""Fetch Zonal Statistics of Weather Indicators for Brazilian
Municipalities

	Fetches zonal statistics from weather indicators that were calculated for each municipality in Brazil using data from the BR-DWGD and TerraClimate projects.
    Zonal statistics such as mean, maximum, minimum, standard deviation, and sum were computed by taking into account the data cells that intersect the boundaries of each municipality and stored in Parquet files. This procedure was carried out for all Brazilian municipalities, and for all available dates, for every indicator available in the weather products (BR-DWGD and TerraClimate projects). This package queries on-line the already calculated statistics on the Parquet files and returns easy-to-use data.frames.
	"""
	
	homepage = "https://rfsaldanha.github.io/brclimr/"
	cran = "brclimr" 

	version("0.1.2", md5="1274e4f3e058e9994c6ddd978248d746")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-lobstr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTuflowr(RPackage):
	"""Helper Functions for 'TUFLOW FV' Models

	Helper functions for 'TUFLOW FV' models. Current functionality includes reading in and plotting
    output POINTS files and generating initial conditions based on point observations.
	"""
	
	homepage = "<https://github.com/matt-s-gibbs/TUFLOWR>"
	cran = "TUFLOWR" 

	version("0.1.1", md5="126b497ac25287f2d1f74f69c37fac9e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))

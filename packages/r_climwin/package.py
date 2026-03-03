# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClimwin(RPackage):
	"""Climate Window Analysis

	Contains functions to detect and visualise periods of climate
    sensitivity (climate windows) for a given biological response. 
    Please see van de Pol et al. (2016) <doi:10.1111/2041-210X.12590> 
    and Bailey and van de Pol (2016) <doi:10.1371/journal.pone.0167980> for details.
	"""
	
	homepage = "https://github.com/LiamDBailey/climwin"
	cran = "climwin" 

	version("1.2.3", md5="dac1da84dc398ac86d00f34b0cc55eaa")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStacomir(RPackage):
	"""Fish Migration Monitoring

	Graphical outputs and treatment for a database of fish pass
    monitoring. It is a part of the 'STACOMI' open source project developed in
    France by the French Office for Biodiversity institute to centralize
    data obtained by fish pass monitoring. This version is available in French and
    English. See <http://stacomir.r-forge.r-project.org/> for more information on
    'STACOMI'.     
	"""
	
	homepage = "http://stacomir.r-forge.r-project.org/"
	cran = "stacomiR" 

	version("0.6.0.7", md5="435f0529fc419a9ea3519c23da35aaeb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-stacomirtools@0.6.0.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-intervals", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rpostgres", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-hmisc@4.1.1:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-pool", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))

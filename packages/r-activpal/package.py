# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActivpal(RPackage):
	"""Advanced Processing and Chart Generation from activPAL Events
Files

	Contains functions to generate pre-defined summary statistics from activPAL
    events files <http:www.palt.com>.  The package also contains functions to produce informative 
    graphics that visualise physical activity behaviour and trends.  This includes
    generating graphs that align physical activity behaviour with additional time based 
    observations described by other data sets, such as sleep diaries and continuous glucose 
    monitoring data.
	"""
	
	cran = "activPAL" 

	version("0.1.3", md5="31beb11c44542e6533bb99e9759b75a4")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))

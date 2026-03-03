# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBirdscanr(RPackage):
	"""Migration Traffic Rate Calculation Package for 'Birdscan MR1'
Radars

	Extract data from 'Birdscan MR1' 'SQL' vertical-looking radar databases, filter, and process them to Migration Traffic Rates (#objects per hour and km) of, for example birds, and insects. Object classifications in the 'Birdscan MR1' databases are based on the dataset of Haest et al. (2021) <doi:10.5281/zenodo.5734960>). Migration Traffic Rates can be calculated separately for different height bins (with a height resolution of choice) as well as over time periods of choice (e.g., 1/2 hour, 1 hour, 1 day, day/night, the full time period of observation, and anything in between). Two plotting functions are also included to explore the data in the 'SQL' databases and the resulting Migration Traffic Rate results. For details on the Migration Traffic Rate calculation procedures, see Schmid et al. (2019) <doi:10.1111/ecog.04025>.
	"""
	
	homepage = "https://github.com/BirdScanCommunity/birdscanR"
	cran = "birdscanR" 

	version("0.2.0", md5="d50ac14873a4f04d4fe40b3012418799")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-suntools", type=("build", "run"))
	depends_on("r-modi", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rodbc", type=("build", "run"))
	depends_on("r-rpostgresql", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))

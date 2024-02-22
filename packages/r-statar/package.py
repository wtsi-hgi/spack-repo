# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatar(RPackage):
	"""Tools Inspired by 'Stata' to Manipulate Tabular Data

	A set of tools inspired by 'Stata' to explore data.frames ('summarize',
    'tabulate', 'xtile', 'pctile', 'binscatter', elapsed quarters/month, lead/lag).
	"""
	
	homepage = "https://github.com/matthieugomez/statar"
	cran = "statar" 

	version("0.7.6", md5="90d3a1c9415d945da5b5c79431b71442")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

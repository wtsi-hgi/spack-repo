# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBupar(RPackage):
	"""Business Process Analysis in R

	Comprehensive Business Process Analysis toolkit. Creates S3-class for event log objects, and related handler functions. Imports related packages for filtering event data, computation of descriptive statistics, handling of 'Petri Net' objects and visualization of process maps. See also packages 'edeaR','processmapR', 'eventdataR' and 'processmonitR'.
	"""
	
	homepage = "https://bupar.net/"
	cran = "bupaR" 

	version("0.5.3", md5="f3d1d517287af231c9ca04b499ef23d1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-cli@3.2:", type=("build", "run"))
	depends_on("r-eventdatar@0.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

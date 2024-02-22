# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSangertools(RPackage):
	"""Tools for Population Health Management Analytics

	Created for population health analytics and monitoring.
    The functions in this package work best when working with patient level Master Patient Index-like datasets .
    Built to be used by  NHS bodies and other health service providers.
	"""
	
	cran = "SangerTools" 

	version("1.0.2", md5="7ab76f7ff424ae7490d73eb4813e3360")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-odbc", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))

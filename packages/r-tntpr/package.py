# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTntpr(RPackage):
	"""Data Analysis Tools Customized for TNTP

	An assortment of functions and templates customized to meet 
    the needs of data analysts at the non-profit organization TNTP. 
    Includes functions for branded colors and plots, credentials management,
    repository set-up, and other common analytic tasks.
	"""
	
	homepage = "https://github.com/tntp/tntpr"
	cran = "tntpr" 

	version("1.0.2", md5="e80bc372c75f567cf8a01910365aea0d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-extrafont", type=("build", "run"))
	depends_on("r-formattable", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-labelled", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisdat(RPackage):
	"""Preliminary Visualisation of Data

	Create preliminary exploratory data visualisations of an entire 
    dataset to identify problems or unexpected features using 'ggplot2'.
	"""
	
	homepage = "https://docs.ropensci.org/visdat/"
	cran = "visdat" 

	version("0.6.0", md5="645b1de71ea95fd8b3975e152e7d5976")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeed(RPackage):
	"""Wrangler for Emergency Events Database

	Makes research involving EMDAT and related datasets easier. These Datasets are manually filled and have several formatting and compatibility issues. Weed aims to resolve these with its functions.
	"""
	
	homepage = "https://github.com/rammkripa/weed"
	cran = "weed" 

	version("1.1.2", md5="66771974c3f011dc16bbe217583cd4f7")

	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-geonames", type=("build", "run"))
	depends_on("r-countrycode", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))

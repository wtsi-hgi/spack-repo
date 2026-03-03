# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpicleanr(RPackage):
	"""A Tidy Solution for Epidemiological Data

	Offers a tidy solution for epidemiological data. It houses a range of functions for epidemiologists and public health data wizards for data management and cleaning.
	"""
	
	homepage = "https://github.com/truenomad/epiCleanr"
	cran = "epiCleanr" 

	version("0.2.0", md5="7725192d0d0e90ec24e829687836c082")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-countrycode", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegions(RPackage):
	"""Processing Regional Statistics

	Validating sub-national statistical typologies, re-coding across 
    standard typologies of sub-national statistics, and making valid aggregate
    level imputation, re-aggregation, re-weighting and projection down to 
    lower hierarchical levels to create meaningful data panels and time series.
	"""
	
	homepage = "https://regions.dataobservatory.eu/"
	cran = "regions" 

	version("0.1.8", md5="02775aa23bdddb5949e8c7c584116ed3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-countrycode", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))

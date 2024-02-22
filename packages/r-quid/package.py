# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuid(RPackage):
	"""Bayesian Mixed Models for Qualitative Individual Differences

	Test whether equality and order constraints hold for all 
    individuals simultaneously by comparing Bayesian mixed models through Bayes 
    factors. A tutorial style vignette and a quickstart guide are available, via
    vignette("manual", "quid"), and vignette("quickstart", "quid") respectively.
    See Haaf and Rouder (2017) <doi:10.1037/met0000156>; Haaf, Klaassen and Rouder
    (2019) <doi:10.31234/osf.io/a4xu9>; and Rouder & Haaf (2021) <doi:10.5334/joc.131>.
	"""
	
	cran = "quid" 

	version("0.0.1", md5="359694da74422100c31e4e1594216b0c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-bayesfactor", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

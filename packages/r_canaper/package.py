# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanaper(RPackage):
	"""Categorical Analysis of Neo- And Paleo-Endemism

	Provides functions to analyze the spatial distribution of
    biodiversity, in particular categorical analysis of neo- and paleo-endemism
    (CANAPE) as described in Mishler et al (2014) <doi:10.1038/ncomms5473>.
    'canaper' conducts statistical tests to determine the types of endemism that
    occur in a study area while accounting for the evolutionary relationships of
    species.
	"""
	
	homepage = "https://github.com/ropensci/canaper"
	cran = "canaper" 

	version("1.0.1", md5="3109710fdf90e91a96173474e5fa02c0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-assertr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-phyloregion", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))

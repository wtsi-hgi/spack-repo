# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbglm(RPackage):
	"""Generalised Linear Models by Subsampling and One-Step Polishing

	Fast fitting of generalised linear models on moderately large datasets, by taking an initial sample, fitting in memory, then evaluating the score function for the full data in the database. Thomas Lumley <doi:10.1080/10618600.2019.1610312>.
	"""
	
	cran = "dbglm" 

	version("1.0.0", md5="b5ed0d45b1c818b1a95f0402b2ebd1ab")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-tidypredict", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

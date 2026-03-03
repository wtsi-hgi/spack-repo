# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModerndive(RPackage):
	"""Tidyverse-Friendly Introductory Linear Regression

	Datasets and wrapper functions for tidyverse-friendly introductory linear regression, used in "Statistical Inference via Data Science: A ModernDive into R and the Tidyverse" available at <https://moderndive.com/>.
	"""
	
	homepage = "https://moderndive.github.io/moderndive/"
	cran = "moderndive" 

	version("0.5.5", md5="9786ade35c7c585fc0d8d9f94cf53444")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-broom@0.4.3:", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-infer", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))

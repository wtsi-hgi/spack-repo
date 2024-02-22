# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrosstable(RPackage):
	"""Crosstables for Descriptive Analyses

	Create descriptive tables for continuous and categorical variables. 
    Apply summary statistics and counting function, with or without a grouping variable, and create beautiful reports using 'rmarkdown' or 'officer'.
    You can also compute effect sizes and statistical tests if needed.
	"""
	
	homepage = "https://danchaltiel.github.io/crosstable/"
	cran = "crosstable" 

	version("0.7.0", md5="f3303fb5af9f439f6199da95c2664194")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-checkmate@1.9:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-flextable@0.5.1:", type=("build", "run"))
	depends_on("r-forcats@1:", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-officer@0.4:", type=("build", "run"))
	depends_on("r-purrr@0.2.3:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@1.1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))

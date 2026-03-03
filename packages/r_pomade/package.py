# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPomade(RPackage):
	"""Power for Meta-Analysis of Dependent Effects

	Provides functions to compute and plot power levels, minimum detectable effect sizes, and minimum required sample sizes for the test of the overall average effect size in meta-analysis of dependent effect sizes.
	"""
	
	homepage = "https://mikkelvembye.github.io/POMADE/"
	cran = "POMADE" 

	version("0.2.0", md5="7c7557076267b505cf0039780de66a9a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))

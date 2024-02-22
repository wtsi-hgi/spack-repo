# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidymodels(RPackage):
	"""Easily Install and Load the 'Tidymodels' Packages

	The tidy modeling "verse" is a collection of packages for
    modeling and statistical analysis that share the underlying design
    philosophy, grammar, and data structures of the tidyverse.
	"""
	
	homepage = "https://tidymodels.tidymodels.org"
	cran = "tidymodels" 

	version("1.1.1", md5="c8a579518108227ff270ef4365dc0d3f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-broom@1.0.5:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
	depends_on("r-conflicted@1.2:", type=("build", "run"))
	depends_on("r-dials@1.2:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.3:", type=("build", "run"))
	depends_on("r-hardhat@1.3:", type=("build", "run"))
	depends_on("r-infer@1.0.4:", type=("build", "run"))
	depends_on("r-modeldata@1.2:", type=("build", "run"))
	depends_on("r-parsnip@1.1.1:", type=("build", "run"))
	depends_on("r-purrr@1.0.2:", type=("build", "run"))
	depends_on("r-recipes@1.0.7:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-rsample@1.2:", type=("build", "run"))
	depends_on("r-rstudioapi@0.15:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-tune@1.1.2:", type=("build", "run"))
	depends_on("r-workflows@1.1.3:", type=("build", "run"))
	depends_on("r-workflowsets@1.0.1:", type=("build", "run"))
	depends_on("r-yardstick@1.2:", type=("build", "run"))

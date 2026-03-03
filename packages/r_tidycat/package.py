# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidycat(RPackage):
	"""Expand Tidy Output for Categorical Parameter Estimates

	Create additional rows and columns on broom::tidy() output to allow for easier control on categorical parameter estimates. 
	"""
	
	homepage = "https://guyabel.github.io/tidycat/"
	cran = "tidycat" 

	version("0.1.2", md5="97bce72f88619f2c1795116c9590e869")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))

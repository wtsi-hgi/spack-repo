# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsemodels(RPackage):
	"""Boilerplate Code for 'Tidymodels' Analyses

	Code snippets to fit models using the tidymodels framework
    can be easily created for a given data set.
	"""
	
	homepage = "https://usemodels.tidymodels.org/"
	cran = "usemodels" 

	version("0.2.0", md5="feb763847d3c5dd684935ded9d69219e")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-recipes@0.1.15:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tune@0.1.2:", type=("build", "run"))

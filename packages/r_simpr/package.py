# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimpr(RPackage):
	"""Flexible 'Tidyverse'-Friendly Simulations

	A general, 'tidyverse'-friendly framework 
  for simulation studies, design analysis, and power analysis. 
  Specify data generation, define varying parameters, generate data, 
  fit models, and tidy model results in a single pipeline, without 
  needing loops or custom functions.
	"""
	
	homepage = "https://statisfactions.github.io/simpr/"
	cran = "simpr" 

	version("0.2.6", md5="ff0aae4828fd68a5b2dbe1b4bf512709")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))

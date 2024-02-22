# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTraitstrap(RPackage):
	"""Bootstrap Trait Values to Calculate Moments

	Calculates trait moments from trait and community data using the 
  methods developed in Maitner et al (2021) <doi:10.22541/au.162196147.76797968/v1>.
	"""
	
	homepage = "https://github.com/Plant-Functional-Trait-Course/traitstrap/"
	cran = "traitstrap" 

	version("0.1.0", md5="1df9b9fadb7859812ff1af322a775122")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))

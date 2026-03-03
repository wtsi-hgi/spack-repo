# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgphazard(RPackage):
	"""Markov Beta and Gamma Processes for Modeling Hazard Rates

	Computes the hazard rate estimate as described by
    Nieto-Barajas & Walker (2002), Nieto-Barajas (2003), Nieto-Barajas &
    Walker (2007) and Nieto-Barajas & Yin (2008).
	"""
	
	homepage = "https://github.com/EAMI91/BGPhazard"
	cran = "BGPhazard" 

	version("2.1.1", md5="95aad871044ca42c284e3e8989a010ed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-brobdingnag", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))

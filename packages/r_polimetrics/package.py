# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolimetrics(RPackage):
	"""R Tools for Political Measures

	This is a collection of data and functions for common metrics in political science research. Data measuring ideology, and functions calculating geographical diffusion and ideological diffusion - geog.diffuse() and ideo.dist(), respectively. Functions derived from methods developed in: Soule and King (2006) <doi:10.1086/499908>, Berry et al. (1998) <doi:10.2307/2991759>, Cruz-Aceves and Mallinson (2019) <doi:10.1177/0160323X20902818>, and Grossback et al. (2004) <doi:10.1177/1532673X04263801>.
	"""
	
	cran = "polimetrics" 

	version("1.2.1.14", md5="b43ca791c19676a6bd452ca2a87a3b2c")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

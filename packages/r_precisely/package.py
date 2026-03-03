# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrecisely(RPackage):
	"""Estimate Sample Size Based on Precision Rather than Power

	Estimate sample size based on precision rather than power.
    'precisely' is a study planning tool to calculate sample size based on
    precision. Power calculations are focused on whether or not an
    estimate will be statistically significant; calculations of precision
    are based on the same principles as power calculation but turn the
    focus to the width of the confidence interval. 'precisely' is based on
    the work of 'Rothman and Greenland' (2018).
	"""
	
	homepage = "https://github.com/malcolmbarrett/precisely"
	cran = "precisely" 

	version("0.1.2", md5="5026cb106d41a380b98972a1c31363c1")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))

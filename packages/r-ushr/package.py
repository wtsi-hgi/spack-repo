# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUshr(RPackage):
	"""Understanding Suppression of HIV

	Analyzes longitudinal data of HIV decline in patients on antiretroviral therapy using the canonical biphasic exponential decay model (pioneered, for example, by work in Perelson et al. (1997) <doi:10.1038/387188a0>; and Wu and Ding (1999) <doi:10.1111/j.0006-341X.1999.00410.x>). Model fitting and parameter estimation are performed, with additional options to calculate the time to viral suppression. Plotting and summary tools are also provided for fast assessment of model results.
	"""
	
	homepage = "https://github.com/SineadMorris/ushr"
	cran = "ushr" 

	version("0.2.3", md5="c1aa7e2221c79f23be99c069682d6879")

	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))

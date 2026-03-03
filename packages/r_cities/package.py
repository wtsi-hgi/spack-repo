# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCities(RPackage):
	"""Clinical Trials with Intercurrent Events Simulator

	Simulates clinical trials and summarizes causal effects and treatment policy estimands in the presence of intercurrent events in a transparent and intuitive manner.
	"""
	
	homepage = "https://hakeemwahabapp.shinyapps.io/cities/"
	cran = "cities" 

	version("0.1.3", md5="63aa532318ecd005dff6b67ff0120400")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))

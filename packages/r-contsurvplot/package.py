# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContsurvplot(RPackage):
	"""Visualize the Effect of a Continuous Variable on a Time-to-Event
Outcome

	Graphically display the (causal) effect of a continuous variable on a time-to-event outcome
	using multiple different types of plots based on g-computation. Those functions
	include, among others, survival area plots, survival contour plots, survival quantile plots and
	3D surface plots. Due to the use of g-computation, all plot allow confounder-adjustment naturally.
	For details, see Robin Denz, Nina Timmesfeld (2023) <doi:10.1097/EDE.0000000000001630>.
	"""
	
	homepage = "https://github.com/RobinDenz1/contsurvplot"
	cran = "contsurvplot" 

	version("0.2.1", md5="b22b05ef01d7f69b96d8dbc44c681cf3")

	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-riskregression", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))

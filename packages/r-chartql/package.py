# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChartql(RPackage):
	"""Simplified Language for Plots and Charts

	Provides a very simple syntax for the user to generate custom plot(s) without having to remember complicated 'ggplot2' syntax. The 'chartql' package uses 'ggplot2' and manages all the syntax complexities internally. As an example, to generate a bar chart of company sales faceted by product category further faceted by season of the year, we simply write: "CHART bar X category, season Y sales".
	"""
	
	homepage = "https://github.com/rmsyed/chartql"
	cran = "chartql" 

	version("0.1.0", md5="040c026717d5852dcb99cb78c0441644")

	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

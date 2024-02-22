# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunnelplotr(RPackage):
	"""Funnel Plots for Comparing Institutional Performance

	An implementation of methods presented by Spiegelhalter (2005) <doi:10.1002/sim.1970> Funnel plots for comparing institutional performance, for standardised ratios, ratios of counts and proportions with additive overdispersion adjustment.
	"""
	
	homepage = "https://nhs-r-community.github.io/FunnelPlotR/"
	cran = "FunnelPlotR" 

	version("0.4.2", md5="2ad3e452a0874af7618d36b04f516c5b")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))

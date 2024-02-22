# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotprjnetworks(RPackage):
	"""Useful Networking Tools for Project Management

	Useful set of tools for plotting network diagrams in any kind of project.
	"""
	
	cran = "PlotPrjNetworks" 

	version("1.0.0", md5="c65405b42c41daadcea6dbdb70b1a0a6")

	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

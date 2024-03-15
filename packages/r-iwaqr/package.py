# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIwaqr(RPackage):
	"""Irrigation Water Quality Assessment and Visualizations

	Calculates irrigation water quality ratios and has functions that could be used to plot several popular diagrams for irrigation water quality classification.
	"""
	
	cran = "iwaqr" 

	version("1.8.4", md5="33e2de4202e1bcf5845af3b7d63ea59a")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQqvases(RPackage):
	"""Animated Normal Quantile-Quantile Plots

	Presents an explanatory animation of normal quantile-quantile plots based on a water-filling analogy.  The animation presents a normal QQ plot as the parametric plot of the water levels in vases defined by two distributions.  The distributions decorate the axes in the normal QQ plot and are optionally shown as vases adjacent to the plot.  The package draws QQ plots for several distributions, either as samples or continuous functions.
	"""
	
	cran = "qqvases" 

	version("1.0.0", md5="97bae2aff82d33d5091466cbb4e7ea63")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))

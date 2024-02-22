# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNostalgir(RPackage):
	"""Advanced Text-Based Plots

	Provides functions to produce advanced ascii graphics, directly to the terminal window. This package utilizes the txtplot() function from the 'txtplot' package, to produce text-based histograms, empirical cumulative distribution function plots, scatterplots with fitted and regression lines, quantile plots, density plots, image plots, and contour plots.
	"""
	
	cran = "NostalgiR" 

	version("1.0.2", md5="6626812f3223af14edcd20b27df2a0db")

	depends_on("r-txtplot", type=("build", "run"))

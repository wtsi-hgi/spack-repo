# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlleleshift(RPackage):
	"""Predict and Visualize Population-Level Changes in Allele
Frequencies in Response to Climate Change

	Methods (<doi:10.7717/peerj.11534>) are provided of calibrating and predicting shifts in allele frequencies through redundancy analysis ('vegan::rda()') and generalized additive models ('mgcv::gam()'). Visualization functions for predicted changes in allele frequencies include 'shift.dot.ggplot()', 'shift.pie.ggplot()', 'shift.moon.ggplot()', 'shift.waffle.ggplot()' and 'shift.surf.ggplot()' that are made with input data sets that are prepared by helper functions for each visualization method. Examples in the documentation show how to prepare animated climate change graphics through a time series with the 'gganimate' package. Function 'amova.rda()' shows how Analysis of Molecular Variance can be directly conducted with the results from redundancy analysis.
	"""
	
	cran = "AlleleShift" 

	version("1.1-2", md5="cc881c2995d5654dde2224124c4f8ec0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-vegan@2.6.4:", type=("build", "run"))
	depends_on("r-biodiversityr@2.15.4:", type=("build", "run"))
	depends_on("r-adegenet", type=("build", "run"))

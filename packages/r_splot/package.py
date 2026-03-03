# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplot(RPackage):
	"""Simplified Plotting for Data Exploration

	Automates common plotting tasks to ease data exploration.
  Makes density plots (potentially overlaid on histograms),
  scatter plots with prediction lines, or bar or line plots with error bars.
  For each type, y, or x and y variables can be plotted at levels of other variables,
  all with minimal specification.
	"""
	
	homepage = "https://miserman.github.io/splot/"
	cran = "splot" 

	version("0.5.4", md5="9dcdb1d0864de07a02a28a4736ee1111")

	depends_on("r@3.1:", type=("build", "run"))

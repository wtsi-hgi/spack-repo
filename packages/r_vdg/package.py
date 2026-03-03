# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVdg(RPackage):
	"""Variance Dispersion Graphs and Fraction of Design Space Plots

	Facilities for constructing variance dispersion graphs, fraction-
    of-design-space plots and similar graphics for exploring the properties of
    experimental designs. The design region is explored via random sampling, which
    allows for more flexibility than traditional variance dispersion graphs. A
    formula interface is leveraged to provide access to complex model formulae.
    Graphics can be constructed simultaneously for multiple experimental designs
    and/or multiple model formulae. Instead of using pointwise optimization to
    find the minimum and maximum scaled prediction variance curves, which can be
    inaccurate and time consuming, this package uses quantile regression as an
    alternative.
	"""
	
	cran = "vdg" 

	version("1.2.2", md5="89be3631bd46d44b76cb13cd9609d138")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))

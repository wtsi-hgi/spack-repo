# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotmo(RPackage):
	"""Plot a Model's Residuals, Response, and Partial Dependence Plots.

	Plot model surfaces for a wide variety of models using partial dependence
	plots and other techniques. Also plot model residuals and other information
	on the model."""

	cran = "plotmo"

	license("GPL-3.0-only")

	version("3.6.3", md5="92a109886fbf544f525c22390171e30c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-formula@1.2.3:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))

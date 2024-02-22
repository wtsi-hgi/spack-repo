# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
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

	version("3.6.2", md5="b2b767006634d5daff7247f4c99e72ca")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-formula@1.2.3:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-teachingdemos", type=("build", "run"))

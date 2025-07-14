# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrmetrics(RPackage):
	"""Calculate growth-rate inhibition (GR) metrics

	Functions for calculating and visualizing growth-rate inhibition (GR) metrics.
	"""
	
	homepage = "https://github.com/uc-bd2k/GRmetrics"
	bioc = "GRmetrics"

	version("1.34.0", commit="a780f6bd8bf1d5b86264b11842853b621cd749ce")
	version("1.28.0", commit="90c38dd21ba83bbb24f817a467b619cafaee0601")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

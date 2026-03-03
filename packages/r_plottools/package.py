# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlottools(RPackage):
	"""Add Continuous Legends to Plots

	Annotate plots with legends for continuous variables and colour
  spectra using the base graphics plotting tools; and manipulate irregular
  polygons.
	"""
	
	homepage = "https://ms609.github.io/PlotTools/"
	cran = "PlotTools" 

	version("0.3.0", md5="660e787ca2b4ea8c2d88caeafd08496e")

	depends_on("r@3.2:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsutils(RPackage):
	"""Time Series Exploration, Modelling and Forecasting

	Includes: (i) tests and visualisations that can help the modeller explore time series components and perform decomposition; (ii) modelling shortcuts, such as functions to construct lagmatrices and seasonal dummy variables of various forms; (iii) an implementation of the Theta method; (iv) tools to facilitate the design of the forecasting process, such as ABC-XYZ analyses; and (v) "quality of life" functions, such as treating time series for trailing and leading values.
	"""
	
	homepage = "https://github.com/trnnick/tsutils/"
	cran = "tsutils" 

	version("0.9.4", md5="a8a0a1fff3f00f0605e4578ba23c9d43")

	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-mapa", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))

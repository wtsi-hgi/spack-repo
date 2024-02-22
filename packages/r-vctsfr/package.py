# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVctsfr(RPackage):
	"""Visualizing Collections of Time Series Forecasts

	A way of visualizing collections of time series and, optionally
    their future values, forecasts for their future values and prediction
    intervals for the forecasts. A web-based GUI can be used to display the
    information in a collection of time series.
	"""
	
	homepage = "https://github.com/franciscomartinezdelrio/vctsfr"
	cran = "vctsfr" 

	version("0.1.1", md5="d0110ff95c9574933785f32dc27ed3be")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))

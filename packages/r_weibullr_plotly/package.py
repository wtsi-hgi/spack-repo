# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeibullrPlotly(RPackage):
	"""Interactive Weibull Probability Plots with 'WeibullR'

	Build interactive Weibull Probability 
  Plots with 'WeibullR' by David Silkworth and Jurgen Symynck (2022) 
  <https://CRAN.R-project.org/package=WeibullR>, an R package for 
  Weibull analysis, and 'plotly' by Carson Sievert (2020) <https://plotly-r.com>, 
  an interactive web-based graphing library.
	"""
	
	homepage = "https://paulgovan.github.io/WeibullR.plotly/"
	cran = "WeibullR.plotly" 

	version("0.2.0", md5="4db44f7960ed542ec6cf2c43d86139d1")

	depends_on("r-weibullr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))

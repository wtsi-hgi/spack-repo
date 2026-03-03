# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeibullrShiny(RPackage):
	"""A 'Shiny' App for Weibull Analysis from 'WeibullR'

	A 'Shiny' web application for life data analysis that depends on 'WeibullR' by David Silkworth and Jurgen Symynck (2022) 
  <https://CRAN.R-project.org/package=WeibullR>, an R package for Weibull analysis.
	"""
	
	homepage = "https://paulgovan.github.io/WeibullR.shiny/"
	cran = "WeibullR.shiny" 

	version("0.2.0", md5="399a135eed3200a3f6bb1b1896a4bd12")

	depends_on("r-weibullr", type=("build", "run"))
	depends_on("r-weibullr-plotly", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))

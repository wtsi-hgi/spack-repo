# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLangevitour(RPackage):
	"""Langevin Tour

	
    An HTML widget that randomly tours 2D projections of numerical data. A random walk through projections of the data is shown. The user can manipulate the plot to use specified axes, or turn on Guided Tour mode to find an informative projection of the data. Groups within the data can be hidden or shown, as can particular axes. Points can be brushed, and the selection can be linked to other widgets using crosstalk. The underlying method to produce the random walk and projection pursuit uses Langevin dynamics. The widget can be used from within R, or included in a self-contained R Markdown or Quarto document or presentation, or used in a Shiny app.
	"""
	
	homepage = "https://logarithmic.net/langevitour/"
	cran = "langevitour" 

	version("0.7", md5="3059fe96ed04e8dcc5b8f67b9e7cb182")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-crosstalk", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistplotter(RPackage):
	"""A Graphical User Interface for Plotting Common Univariate
Distributions

	Package including an interactive Shiny application for plotting 
    common univariate distributions.
	"""
	
	homepage = "https://github.com/ccasement/DistPlotter"
	cran = "DistPlotter" 

	version("0.0.2", md5="95d7c94c8e14497151c3adf33ff6bd47")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-colourpicker@1.1.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.8:", type=("build", "run"))
	depends_on("r-dt@0.20:", type=("build", "run"))
	depends_on("r-extradistr@1.9.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-rio@0.5.29:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-shinyalert@3:", type=("build", "run"))
	depends_on("r-shinybs@0.61:", type=("build", "run"))
	depends_on("r-shinyjs@2.1:", type=("build", "run"))
	depends_on("r-shinywidgets@0.6.4:", type=("build", "run"))
	depends_on("r-stringi@1.7.6:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))

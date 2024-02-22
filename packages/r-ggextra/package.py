# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgextra(RPackage):
	"""Add Marginal Histograms to 'ggplot2', and More 'ggplot2'
Enhancements

	Collection of functions and layers to enhance 'ggplot2'. The 
    flagship function is 'ggMarginal()', which can be used to add marginal
    histograms/boxplots/density plots to 'ggplot2' scatterplots.
	"""
	
	homepage = "https://github.com/daattali/ggExtra"
	cran = "ggExtra" 

	version("0.10.1", md5="831b5f3748fe1a3cce93491adfe844f9")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-colourpicker@1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-gtable@0.2:", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-scales@0.2:", type=("build", "run"))
	depends_on("r-shiny@0.13:", type=("build", "run"))
	depends_on("r-shinyjs@0.5.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))

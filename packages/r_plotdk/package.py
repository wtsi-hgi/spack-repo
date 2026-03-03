# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotdk(RPackage):
	"""Plot Summary Statistics as Choropleth Maps of Danish
Administrative Areas

	Provides a ggplot2 front end to plot summary statistics on danish provinces,
    regions, municipalities, and zipcodes. The needed geoms of each of the four levels are 
    inherent in the package, thus making these types of plots easy for the user. This is essentially 
    an updated port of the previously available 'mapDK' package by Sebastian Barfort.
	"""
	
	cran = "plotDK" 

	version("0.1.0", md5="9a022c6e90492a54f0c3f738a3d52781")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-mapproj", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))

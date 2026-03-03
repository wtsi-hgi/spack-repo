# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROceanexplorer(RPackage):
	"""Explore Our Planet's Oceans with NOAA

	Provides tools for easy exploration of the world ocean atlas of 
  the US agency National Oceanic and Atmospheric Administration (NOAA). It 
  includes functions to extract NetCDF data from the repository and code to 
  visualize several physical and chemical parameters of the ocean. A Shiny app 
  further allows interactive exploration of the data. The methods for data 
  collecting and quality checks are described in several papers, which can be
  found here: <https://www.ncei.noaa.gov/products/world-ocean-atlas>.
	"""
	
	homepage = "https://martinschobben.github.io/oceanexplorer/"
	cran = "oceanexplorer" 

	version("0.1.0", md5="b02950e5be4c338a8124a8fd650b0a2f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-stars@0.5.5:", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-sf@1.0.5:", type=("build", "run"))
	depends_on("r-waiter@0.2.5:", type=("build", "run"))
	depends_on("r-bslib@0.3.1:", type=("build", "run"))
	depends_on("r-thematic@0.1.2.1:", type=("build", "run"))
	depends_on("r-shinyfeedback@0.4:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-miniui@0.1.1.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.13:", type=("build", "run"))
	depends_on("r-dt@0.20:", type=("build", "run"))
	depends_on("r-fs@1.5.2:", type=("build", "run"))
	depends_on("r-glue@1.6:", type=("build", "run"))
	depends_on("r-shinyjs@2.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-maps@3.4:", type=("build", "run"))
	depends_on("r-ncmeta@0.3:", type=("build", "run"))
	depends_on("r-rnetcdf@2.6.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))

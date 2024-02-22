# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRassta(RPackage):
	"""Raster-Based Spatial Stratification Algorithms

	Algorithms for the spatial stratification of landscapes, sampling and modeling of 
    spatially-varying phenomena. These algorithms offer a simple framework for the stratification 
    of geographic space based on raster layers representing landscape factors and/or factor scales. 
    The stratification process follows a hierarchical approach, which is based on first level units 
    (i.e., classification units) and second-level units (i.e., stratification units). Nonparametric 
    techniques allow to measure the correspondence between the geographic space and the landscape 
    configuration represented by the units. These correspondence metrics are useful to define 
    sampling schemes and to model the spatial variability of environmental phenomena. The 
    theoretical background of the algorithms and code examples are presented in Fuentes, Dorantes,
    and Tipton (2021). <doi:10.31223/X50S57>.
	"""
	
	homepage = "https://bafuentes.github.io/rassta/"
	cran = "rassta" 

	version("1.0.5", md5="997249a3aea3afb899d1d692c55f785f")

	depends_on("r-cluster@2.1.2:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-dt@0.18:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-ggally@2.1.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-histogram@0.0.25:", type=("build", "run"))
	depends_on("r-kernsmooth@2.23.18:", type=("build", "run"))
	depends_on("r-kohonen@3.0.10:", type=("build", "run"))
	depends_on("r-plotly@4.9.4.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-stringdist@0.9.6.3:", type=("build", "run"))
	depends_on("r-stringi@1.7.2:", type=("build", "run"))
	depends_on("r-terra@1.3.4:", type=("build", "run"))

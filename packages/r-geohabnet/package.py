# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeohabnet(RPackage):
	"""Analysis of Cropland Connectivity

	
    Geographical spatial analysis of cropland connectivity.
    Allows users to visualize risk index plots for a given set of crops.
    The functions are developed as an extension to analysis from Xing et al (2021) <doi:10.1093/biosci/biaa067>.
    The primary function is sean() and is indicative of how sensitive the risk analysis is to parameters using kernel models.
    The Package currently supports crops sourced from Monfreda, C., N. Ramankutty, and J. A. Foley (2008) <doi:10.1029/2007gb002947> "Farming the planet: 2. Geographic distribution of crop areas, yields, physiological types, and net primary production in the year 2000, Global Biogeochem. Cycles, 22, GB1022" and
    International Food Policy Research Institute (2019) <doi:10.7910/DVN/PRFF8V> "Global Spatially-Disaggregated Crop Production Statistics Data for 2010 Version 2.0, Harvard Dataverse, V4".
    This analysis produces 3 maps - mean, variance, and difference for the crop risk index. It applies distance functions and graph operations on a network to calculate risk index.
    There are multiple ways in which functions can be used - generate final outcome and then the intermediate outcomes for more sophisticated use cases.
    Refer to vignettes.
    sean() will set some global variables which can be accessed using $ prefix. These values are propagated to other functions for performing operations such as distance matrix calculation.
    parameters.yaml stores the parameters and values and can be accessed using get_parameters(). Refer it's usage.
    The objective of this package is to support risk analysis using cropland connectivity on 10 parameters -
    host crops, density threshold, aggregation and distance method, resolution, geographic extent, link threshold, kernel models, network metrics and maps.
    These parameters serves as an input and are used different phases of analysis workflow.
	"""
	
	homepage = "https://garrettlab.github.io/CroplandConnectivity/"
	cran = "geohabnet" 

	version("1.0.1", md5="660555e5c660855c020050f8becb1040")

	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-geodata@0.5.8:", type=("build", "run"))
	depends_on("r-geosphere@1.5.18:", type=("build", "run"))
	depends_on("r-igraph@1.4.2:", type=("build", "run"))
	depends_on("r-terra@1.7.29:", type=("build", "run"))
	depends_on("r-easycsv@1.0.8:", type=("build", "run"))
	depends_on("r-yaml@2.3.7:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-memoise@2.0.1:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-viridislite@0.4.2:", type=("build", "run"))
	depends_on("r-beepr@1.3:", type=("build", "run"))
	depends_on("r-rnaturalearth@0.3.3:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenland(RPackage):
	"""Quantitative Analysis and Visualization of LUCC

	Tools for the analysis of land use and cover (LUC) time series. It 
    includes support for loading spatiotemporal raster data and synthesized 
    spatial plotting. Several LUC change (LUCC) metrics in regular or irregular 
    time intervals can be extracted and visualized through one- and multistep 
    sankey and chord diagrams. A complete intensity analysis according to 
    Aldwaik and Pontius (2012) <doi:10.1016/j.landurbplan.2012.02.010> is 
    implemented, including tools for the generation of standardized multilevel 
    output graphics.
	"""
	
	homepage = "https://github.com/reginalexavier/OpenLand"
	cran = "OpenLand" 

	version("1.0.2", md5="eef2ee2cfeef864c94f5943d59584d54")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-circlize@0.4.8:", type=("build", "run"))
	depends_on("r-networkd3@0.4:", type=("build", "run"))
	depends_on("r-raster@3.0.7:", type=("build", "run"))

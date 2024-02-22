# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMazamaspatialplots(RPackage):
	"""Thematic Plots for Mazama Spatial Datasets

	A suite of convenience functions for generating US state and county
    thematic maps using datasets from the MazamaSpatialUtils package.
	"""
	
	homepage = "https://github.com/MazamaScience/MazamaSpatialPlots"
	cran = "MazamaSpatialPlots" 

	version("0.2.0", md5="b1d923e8200fd470c3da1990f5de2b96")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mazamaspatialutils@0.8:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mazamacoreutils@0.4.6:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tmap", type=("build", "run"))

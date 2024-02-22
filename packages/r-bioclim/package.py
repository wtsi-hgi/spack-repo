# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioclim(RPackage):
	"""Bioclimatic Analysis and Classification

	Using numeric or raster data, this package contains functions to 
    calculate: complete water balance, bioclimatic balance, bioclimatic 
    intensities, reports for individual locations, multi-layered rasters for
    spatial analysis.
	"""
	
	cran = "bioclim" 

	version("0.4.0", md5="09a010c65c01aa39a8b23ea72f758847")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-berryfunctions", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))

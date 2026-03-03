# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSomspace(RPackage):
	"""Spatial Analysis with Self-Organizing Maps

	Application of the Self-Organizing Maps technique for spatial classification of time series. The package uses spatial data, point or gridded, to create clusters with similar characteristics. The clusters can be further refined to a smaller number of regions by hierarchical clustering and their spatial dependencies can be presented as complex networks. Thus, meaningful maps can be created, representing the regional heterogeneity of a single variable. More information and an example of implementation can be found in Markonis and Strnad (2020, <doi:10.1177/0959683620913924>).
	"""
	
	cran = "somspace" 

	version("1.2.4", md5="ae124c80ebcacf7603044c91f5f58a8c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-kohonen", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))

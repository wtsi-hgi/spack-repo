# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeatmaps(RPackage):
	"""Heatmaps for Multiple Network Data

	Simplify the exploratory data analysis process for multiple network
             data sets with the help of hierarchical clustering, consensus 
             clustering and heatmaps. Multiple network data consists of multiple
             disjoint networks that have common variables (e.g. ego networks). 
             This package contains the necessary tools for exploring such data,
             from the data pre-processing stage to the creation of dynamic
             visualizations.
	"""
	
	homepage = "https://github.com/PhilBoileau/neatmaps"
	cran = "neatmaps" 

	version("2.1.0", md5="807b38bfe99bb9bc26e02b217a79bf3d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-consensusclusterplus", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))

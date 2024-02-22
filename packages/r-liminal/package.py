# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiminal(RPackage):
	"""Multivariate Data Visualization with Tours and Embeddings

	Compose interactive visualisations designed for exploratory 
        high-dimensional data analysis. With 'liminal' you can create linked
        interactive graphics to diagnose the quality of a dimension reduction
        technique and explore the global structure of a dataset with a tour. A
        complete description of the method is discussed in 
        ['Lee' & 'Laa' & 'Cook' (2020) <arXiv:2012.06077>].
	"""
	
	homepage = "https://github.com/sa-lee/liminal/"
	cran = "liminal" 

	version("0.1.2", md5="d1f04c9c8b5210aa692aabfdebee4c61")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-tourr@0.6:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-vegawidget", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))

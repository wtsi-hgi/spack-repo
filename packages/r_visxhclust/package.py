# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisxhclust(RPackage):
	"""A Shiny App for Visual Exploration of Hierarchical Clustering

	A Shiny application and functions for visual exploration of hierarchical clustering with numeric datasets. Allows users to iterative set hyperparameters, select features and evaluate results through various plots and computation of evaluation criteria.
	"""
	
	homepage = "https://github.com/rhenkin/visxhclust"
	cran = "visxhclust" 

	version("1.1.0", md5="a87beb46a33adedf1539841dd04b2e23")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyhelper", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-bsplus", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-clvalid", type=("build", "run"))
	depends_on("r-dunn-test", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwamp(RPackage):
	"""Visualization, Analysis and Adjustment of High-Dimensional Data
in Respect to Sample Annotations

	Collection of functions to connect the structure of the data with the information on the samples. Three types of associations are covered: 1. linear model of principal components. 2. hierarchical clustering analysis. 3. distribution of features-sample annotation associations. Additionally, the inter-relation between sample annotations can be analyzed. Simple methods are provided for the correction of batch effects and removal of principal components.
	"""
	
	cran = "swamp" 

	version("1.5.1", md5="0d82bed98ce2151090e8a2018fbeeca5")

	depends_on("r-impute", type=("build", "run"))
	depends_on("r-amap", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBpca(RPackage):
	"""Biplot of Multivariate Data Based on Principal Components
Analysis

	Implements biplot (2d and 3d) of multivariate data based
             on principal components analysis and diagnostic tools of the quality of the reduction.
	"""
	
	cran = "bpca" 

	version("1.3-6", md5="ceffa4bb51831795759a84f735055f3e")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaresid(RPackage):
	"""Correspondence Analysis Plot and Associations Visualisation

	Performs a Correspondence Analysis (CA) on a contingency table and creates a scatterplot of the row and column points on the selected dimensions. Optionally, the function can add segments to the plot to visualize significant associations between row and column categories on the basis of positive (unadjusted) standardized residuals larger than a given threshold.
	"""
	
	cran = "caresid" 

	version("0.1", md5="1a8339fd49aba87fa3d10a1581d0110e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ca@0.71:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggrepel@0.9:", type=("build", "run"))

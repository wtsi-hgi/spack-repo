# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdpens(RPackage):
	"""Selection, Fusion, Smoothing and Principal Components Analysis
for Ordinal Variables

	Selection, fusion, and/or smoothing of ordinally scaled independent variables using a group lasso, fused lasso or generalized ridge penalty, as well as non-linear principal components analysis for ordinal variables using a second-order difference/smoothing penalty.
	"""
	
	cran = "ordPens" 

	version("1.1.0", md5="29eb8341173f38d4f028a706da4e7c04")

	depends_on("r-grplasso", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rlrsim", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-glmpath", type=("build", "run"))
	depends_on("r-ordinalnet", type=("build", "run"))

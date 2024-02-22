# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmridge(RPackage):
	"""Gaussian Graphical Models Using Ridge Penalty Followed by
Thresholding and Reestimation

	Estimation of partial correlation matrix using ridge penalty 
    followed by thresholding and reestimation. Under multivariate Gaussian 
    assumption, the matrix constitutes an Gaussian graphical model (GGM).
	"""
	
	cran = "GGMridge" 

	version("1.4", md5="d05289c5623e8ca7e62843475c1bb4a0")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

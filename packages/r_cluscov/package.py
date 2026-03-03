# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCluscov(RPackage):
	"""Clustered Covariate Regression

	Clustered covariate regression enables estimation and inference in 
 both linear and non-linear models with linear predictor functions even when the
 design matrix is column rank deficient. Routines in this package implement algorithms
 in Soale and Tsyawo (2019) <doi:10.13140/RG.2.2.32355.81441>.
	"""
	
	cran = "cluscov" 

	version("1.1.0", md5="ce4c7c2866f4e2e956e0d9d8f5a3ec27")

	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

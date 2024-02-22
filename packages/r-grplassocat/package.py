# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrplassocat(RPackage):
	"""Standardization for Group Lasso Models with Categorical
Predictors

	Implements the simple and computationally efficient standardization scheme for group lasso models with categorical predictors described in Detmer, Cebral, Slawski (2019) <arXiv:1805.06915>. 
	"""
	
	cran = "grplassocat" 

	version("1.0", md5="9b6bbe0bd703e41dc7ada2fc7f76e2ea")

	depends_on("r-grplasso", type=("build", "run"))

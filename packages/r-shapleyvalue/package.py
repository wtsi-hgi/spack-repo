# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShapleyvalue(RPackage):
	"""Shapley Value Regression for Relative Importance of Attributes

	Shapley Value Regression for calculating the relative importance of independent variables in linear regression with avoiding the collinearity.
	"""
	
	cran = "ShapleyValue" 

	version("0.2.0", md5="753734f70ef5a40e08df2fd4faae82ec")

	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

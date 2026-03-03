# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcovr(RPackage):
	"""Principal Covariates Regression

	Analyzing regression data with many and/or highly collinear predictor variables, by simultaneously reducing the predictor variables to a limited number of components and regressing the criterion variables on these components (de Jong S. & Kiers H. A. L. (1992) <doi:10.1016/0169-7439(92)80100-I>). Several rotation and model selection options are provided.
	"""
	
	cran = "PCovR" 

	version("2.7.2", md5="d28d92246ca468b8f822e2762317aa91")

	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-threeway", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

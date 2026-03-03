# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinearregressionmde(RPackage):
	"""Minimum Distance Estimation in Linear Regression Model

	Consider linear regression model Y = Xb + error where the distribution function of errors is unknown, but errors are independent and symmetrically distributed. The package contains a function named LRMDE which takes Y and X as input and returns minimum distance estimator of parameter b in the model. 
	"""
	
	cran = "LinearRegressionMDE" 

	version("1.0", md5="b6adb3bd9e0e7d88202c4f30583dc696")

	depends_on("r@3.2.2:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClpm(RPackage):
	"""Constrained Estimation of Linear Probability Model

	Estimation of linear model with predictions inside the (0,1) interval. Standard least squares criterion is minimized subjected to a penalty term that enforces the constraints. The estimator is suitable for binary responses, or any response between 0 and 1.
	"""
	
	cran = "clpm" 

	version("1.0", md5="db1aab1d9dac88093ffa0a7a60494427")


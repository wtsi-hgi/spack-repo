# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpmr(RPackage):
	"""Nuclear Penalized Multinomial Regression

	Fit multinomial logistic regression with a penalty on the nuclear
    norm of the estimated regression coefficient matrix, using proximal
    gradient descent.
	"""
	
	cran = "npmr" 

	version("1.3.1", md5="8a28708db2da78b3433c45e587b310bc")

	depends_on("r-matrix", type=("build", "run"))

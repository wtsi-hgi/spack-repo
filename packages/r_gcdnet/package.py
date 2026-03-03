# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcdnet(RPackage):
	"""The (Adaptive) LASSO and Elastic Net Penalized Least Squares,
Logistic Regression, Hybrid Huberized Support Vector Machines,
Squared Hinge Loss Support Vector Machines and Expectile
Regression using a Fast Generalized Coordinate Descent
Algorithm

	Implements a generalized coordinate descent (GCD) algorithm
    for computing the solution paths of the hybrid Huberized support vector
    machine (HHSVM) and its generalizations. Supported models include the
    (adaptive) LASSO and elastic net penalized least squares, logistic
    regression, HHSVM, squared hinge loss SVM and expectile regression.
	"""
	
	homepage = "https://github.com/emeryyi/gcdnet"
	cran = "gcdnet" 

	version("1.0.6", md5="5ed3756f19f05c793eff62327c59352b")

	depends_on("r-matrix", type=("build", "run"))

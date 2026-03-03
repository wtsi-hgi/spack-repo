# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayessampling(RPackage):
	"""Bayes Linear Estimators for Finite Population

	Allows the user to apply the Bayes Linear approach to finite population with the Simple Random Sampling - BLE_SRS() - and
    the Stratified Simple Random Sampling design - BLE_SSRS() - (both without replacement), to the Ratio estimator (using auxiliary
    information) - BLE_Ratio() - and to categorical data - BLE_Categorical().
    The Bayes linear estimation approach is applied to a general linear regression model for finite population prediction in BLE_Reg()
    and it is also possible to achieve the design based estimators using vague prior distributions.    
    Based on Gonçalves, K.C.M, Moura, F.A.S and  Migon, H.S.(2014) <https://www150.statcan.gc.ca/n1/en/catalogue/12-001-X201400111886>.
	"""
	
	homepage = "https://www150.statcan.gc.ca/n1/en/catalogue/12-001-X201400111886"
	cran = "BayesSampling" 

	version("1.1.0", md5="e8e60c7a2ec1f4bf1f6312a041a0de0a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))

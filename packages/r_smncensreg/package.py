# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmncensreg(RPackage):
	"""Fitting Univariate Censored Regression Model Under the Family of
Scale Mixture of Normal Distributions

	Fit univariate right, left or interval censored regression model under the scale mixture of normal distributions.
	"""
	
	cran = "SMNCensReg" 

	version("3.1", md5="226a3079e8a25c913fe3caace1cb0368")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))

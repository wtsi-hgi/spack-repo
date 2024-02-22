# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLbm(RPackage):
	"""Log Binomial Regression Model in Exact Method

	Fit the log binomial regression model (LBM) by Exact method. Limited parameter space of 
    LBM causes trouble to find admissible estimates and fail to converge when MLE is close to or on 
    the boundary of space. Exact method utilizes the property of boundary vectors to re-parametrize 
    the model without losing any information, and fits the model on the standard fitting algorithm 
    with no convergence issues. 
	"""
	
	cran = "lbm" 

	version("0.9.0.2", md5="f808264dd339cef1a38ecefc5e5a0e45")

	depends_on("r@3.5:", type=("build", "run"))

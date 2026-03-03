# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCap(RPackage):
	"""Covariate Assisted Principal (CAP) Regression for Covariance
Matrix Outcomes

	Performs Covariate Assisted Principal (CAP) Regression for covariance matrix outcomes. The method identifies the optimal projection direction which maximizes the log-likelihood function of the log-linear heteroscedastic regression model in the projection space. See Zhao et al. (2018), Covariate Assisted Principal Regression for Covariance Matrix Outcomes, <doi:10.1101/425033> for details.
	"""
	
	cran = "cap" 

	version("1.0", md5="789506f824f97d03812ecd746b884368")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-multigroup", type=("build", "run"))

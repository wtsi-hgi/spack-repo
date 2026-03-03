# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvglmmrank(RPackage):
	"""Multivariate Generalized Linear Mixed Models for Ranking Sports
Teams

	Maximum likelihood estimates are obtained via an EM algorithm with either a first-order or a fully exponential Laplace approximation as documented by Broatch and Karl (2018) <doi:10.48550/arXiv.1710.05284>,
    Karl, Yang, and Lohr (2014) <doi:10.1016/j.csda.2013.11.019>, and by 
	Karl (2012) <doi:10.1515/1559-0410.1471>. Karl and Zimmerman <doi:10.1016/j.jspi.2020.06.004> use this package to illustrate how the home field effect estimator from a mixed model can be biased under nonrandom scheduling. 
	"""
	
	cran = "mvglmmRank" 

	version("1.2-4", md5="5448168c4e2a98ddd36843c74962eab5")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

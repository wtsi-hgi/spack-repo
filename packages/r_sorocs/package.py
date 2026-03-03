# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSorocs(RPackage):
	"""A Bayesian Semiparametric Approach to Correlated ROC Surfaces

	A Bayesian semiparametric Dirichlet process mixtures to estimate correlated receiver operating characteristic (ROC) surfaces and the associated volume under the surface (VUS) with stochastic order constraints. The reference paper is:Zhen Chen, Beom Seuk Hwang, (2018) "A Bayesian semiparametric approach to correlated ROC surfaces with stochastic order constraints". Biometrics, 75, 539-550. <doi:10.1111/biom.12997>. 
	"""
	
	homepage = "http://github.com/wzhang17/sorocs.git"
	cran = "sorocs" 

	version("0.1.0", md5="a01771632504d5d974861db1159521ee")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))

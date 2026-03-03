# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlsrbeta(RPackage):
	"""Partial Least Squares Regression for Beta Regression Models

	Provides Partial least squares Regression for (weighted) beta regression models (Bertrand 2013,  <http://journal-sfds.fr/article/view/215>) and k-fold cross-validation of such models using various criteria. It allows for missing data in the explanatory variables. Bootstrap confidence intervals constructions are also available.
	"""
	
	homepage = "https://fbertran.github.io/plsRbeta/"
	cran = "plsRbeta" 

	version("0.3.0", md5="b06c13363023a0219ed07740c3cd0c20")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plsrglm", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))

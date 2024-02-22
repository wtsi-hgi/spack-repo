# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolywog(RPackage):
	"""Bootstrapped Basis Regression with Oracle Model Selection

	Routines for flexible functional form estimation via basis
    regression, with model selection via the adaptive LASSO or SCAD to prevent
    overfitting.
	"""
	
	homepage = "https://github.com/brentonk/polywog-package"
	cran = "polywog" 

	version("0.4-1", md5="fd542b989caa4a0c236f769a638b4351")

	depends_on("r-misctools@0.6.12:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-glmnet@1.9.5:", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ncvreg@2.4.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoostrq(RPackage):
	"""Boosting Regression Quantiles

	Boosting Regression Quantiles is a component-wise boosting algorithm, 
             that embeds all boosting steps in the well-established framework 
             of quantile regression. It is initialized with the corresponding quantile, 
             uses a quantile-specific learning rate, and uses quantile regression as its base learner.
             The package implements this algorithm and allows cross-validation and stability selection. 
	"""
	
	homepage = "https://github.com/stefanlinner/boostrq"
	cran = "boostrq" 

	version("1.0.0", md5="8d01d5cc4066c19a40370741aff54752")

	depends_on("r-mboost", type=("build", "run"))
	depends_on("r-stabs", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))

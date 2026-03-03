# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbc(RPackage):
	"""Tools for Approximate Bayesian Computation (ABC)

	Implements several ABC algorithms for
        performing parameter estimation, model selection, and goodness-of-fit.
        Cross-validation tools are also available for measuring the
        accuracy of ABC estimates, and to calculate the
        misclassification probabilities of different models.
	"""
	
	cran = "abc" 

	version("2.2.1", md5="21e4c928a8cdd4c6fe3c1c76c99913a9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-abc-data", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))

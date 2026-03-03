# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulvariaterandomforestvarimp(RPackage):
	"""Variable Importance Measures for Multivariate Random Forests

	Calculates two sets of post-hoc variable importance measures for multivariate random forests. The first set of variable importance measures are given by the sum of mean split improvements for splits defined by feature j measured on user-defined examples (i.e., training or testing samples). The second set of importance measures are calculated on a per-outcome variable basis as the sum of mean absolute difference of node values for each split defined by feature j measured on user-defined examples (i.e., training or testing samples). The user can optionally threshold both sets of importance measures to include only splits that are statistically significant as measured using an F-test. 
	"""
	
	homepage = "https://github.com/Megatvini/VIM/"
	cran = "MulvariateRandomForestVarImp" 

	version("0.0.2", md5="8ae658298e5024cc5433bc27ff0e8c36")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-multivariaterandomforest@1.1.5:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))

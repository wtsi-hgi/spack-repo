# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBssn(RPackage):
	"""Birnbaum-Saunders Model

	It provides the density, distribution function, quantile function, random number generator, reliability function, failure rate, likelihood function, moments and EM algorithm for Maximum Likelihood estimators, also empirical quantile and generated envelope for a given sample, all this for the three parameter Birnbaum-Saunders model based on Skew-Normal Distribution. Also, it provides the random number generator for the mixture of Birnbaum-Saunders model based on Skew-Normal distribution. Additionally, we incorporate the EM algorithm based on the assumption that the error term follows a finite mixture of Sinh-normal distributions.
	"""
	
	cran = "bssn" 

	version("1.0", md5="2a5ae82376fe704c54ca5c7b33879c42")

	depends_on("r-sn", type=("build", "run"))
	depends_on("r-ssmn", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-clusterr", type=("build", "run"))

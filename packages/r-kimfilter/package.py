# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKimfilter(RPackage):
	"""Kim Filter

	'Rcpp' implementation of the multivariate Kim filter, which combines the Kalman and Hamilton filters for state probability inference. 
  The filter is designed for state space models and can handle missing values and exogenous data in the observation and state equations.
  Kim, Chang-Jin and Charles R. Nelson (1999) "State-Space Models with Regime Switching: Classical and Gibbs-Sampling Approaches with Applications" <doi:10.7551/mitpress/6444.001.0001><http://econ.korea.ac.kr/~cjkim/>. 
	"""
	
	cran = "kimfilter" 

	version("1.0.3", md5="35edcc925344249a1aec67314b547b35")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

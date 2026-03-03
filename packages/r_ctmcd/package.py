# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtmcd(RPackage):
	"""Estimating the Parameters of a Continuous-Time Markov Chain from
Discrete-Time Data

	Estimation of Markov generator matrices from discrete-time observations. The implemented approaches comprise diagonal and weighted adjustment of matrix logarithm based candidate solutions as in Israel (2001) <doi:10.1111/1467-9965.00114> as well as a quasi-optimization approach. Moreover, the expectation-maximization algorithm and the Gibbs sampling approach of Bladt and Sorensen (2005) <doi:10.1111/j.1467-9868.2005.00508.x> are included.
	"""
	
	cran = "ctmcd" 

	version("1.4.4", md5="e1c1764e64c914c396eec763383ee16c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

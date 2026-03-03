# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcl(RPackage):
	"""Testing in Conditional Likelihood Context

	An implementation of hypothesis testing in an extended Rasch modeling framework,
    including sample size planning procedures and power computations. Provides 4 statistical tests, 
    i.e., gradient test (GR), likelihood ratio test (LR), Rao score or Lagrange multiplier test (RS), 
    and Wald test, for testing a number of hypotheses referring to the Rasch model (RM), linear 
    logistic test model (LLTM), rating scale model (RSM), and partial credit model (PCM). Three 
    types of functions for power and sample size computations are provided. Firstly, functions to 
    compute the sample size given a user-specified (predetermined) deviation from the hypothesis 
    to be tested, the level alpha, and the power of the test. Secondly, functions to evaluate the 
    power of the tests given a user-specified (predetermined) deviation from the hypothesis to be 
    tested, the level alpha of the test, and the sample size. Thirdly, functions to evaluate the 
    so-called post hoc power of the tests. This is the power of the tests given the observed 
    deviation of the data from the hypothesis to be tested and a user-specified level alpha of the
    test. Power and sample size computations are based on a Monte Carlo simulation approach. It is
    computationally very efficient. The variance of the random error in computing power and sample
    size arising from the simulation approach is analytically derived by using the delta method. 
    Draxler, C., & Alexandrowicz, R. W. (2015), <doi:10.1007/s11336-015-9472-y>.
	"""
	
	cran = "tcl" 

	version("0.2.0", md5="ae3857688f65ffde78d54c1102677677")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-erm", type=("build", "run"))
	depends_on("r-psychotools", type=("build", "run"))
	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))

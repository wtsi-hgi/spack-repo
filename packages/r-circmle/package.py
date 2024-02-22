# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircmle(RPackage):
	"""Maximum Likelihood Analysis of Circular Data

	A series of wrapper functions to
    implement the 10 maximum likelihood models of animal orientation
    described by Schnute and Groot (1992) <DOI:10.1016/S0003-3472(05)80068-5>. The
    functions also include the ability to use different optimizer
    methods and calculate various model selection metrics (i.e., AIC,
    AICc, BIC).  The ability to perform variants of the Hermans-Rasson test and
    Pycke test is also included as described in Landler et al. (2019) 
    <DOI:10.1186/s12898-019-0246-8>. The latest version also includes a new
    method to calculate circular-circular and circular-linear distance correlations. 
	"""
	
	homepage = "https://www.r-project.org"
	cran = "CircMLE" 

	version("0.3.0", md5="ed4ada84a74960a4d1cbfe75b51747a4")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-circular@0.4.7:", type=("build", "run"))
	depends_on("r-energy@1.7.7:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFourpno(RPackage):
	"""Bayesian 4 Parameter Item Response Model

	Estimate Barton & Lord's (1981) <doi:10.1002/j.2333-8504.1981.tb01255.x> 
    four parameter IRT model with lower and upper asymptotes using Bayesian
    formulation described by Culpepper (2016) <doi:10.1007/s11336-015-9477-6>.
	"""
	
	homepage = "https://github.com/tmsalab/fourPNO"
	cran = "fourPNO" 

	version("1.1.0", md5="7b006a214697b087a53ae4be56965078")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.200:", type=("build", "run"))

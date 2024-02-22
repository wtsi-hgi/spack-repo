# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppsmc(RPackage):
	"""Rcpp Bindings for Sequential Monte Carlo

	R access to the Sequential Monte Carlo Template Classes
 by Johansen <doi:10.18637/jss.v030.i06> is provided. At present, four
 additional examples have been added, and the first example from the JSS
 paper has been extended. Further integration and extensions are planned.
	"""
	
	homepage = "https://github.com/rcppsmc/rcppsmc"
	cran = "RcppSMC" 

	version("0.2.7", md5="7d0450501a23be7ba0e776d2a0291727")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fkf", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

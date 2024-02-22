# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppnumerical(RPackage):
	"""'Rcpp' Integration for Numerical Computing Libraries

	A collection of open source libraries for numerical computing
    (numerical integration, optimization, etc.) and their integration with
    'Rcpp'.
	"""
	
	homepage = "https://github.com/yixuan/RcppNumerical"
	cran = "RcppNumerical" 

	version("0.6-0", md5="df7acef7a75638390c3024851ba2e4d5")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

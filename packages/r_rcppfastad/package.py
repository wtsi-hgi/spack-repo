# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppfastad(RPackage):
	"""'Rcpp' Bindings to 'FastAD' Auto-Differentiation

	The header-only 'C++' template library 'FastAD' for automatic
 differentiation <https://github.com/JamesYang007/FastAD> is provided by
 this package, along with a few illustrative examples that can all be called
 from R.
	"""
	
	homepage = "https://github.com/eddelbuettel/rcppfastad"
	cran = "RcppFastAD" 

	version("0.0.2", md5="7e1150fc508653beceb8d2d3ecdfbdae")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))

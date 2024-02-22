# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppnloptexample(RPackage):
	"""'Rcpp' Package Illustrating Header-Only Access to 'NLopt'

	An example package which shows use of 'NLopt' functionality from
 C++ via 'Rcpp' without requiring linking, and relying just on 'nloptr' thanks
 to the exporting API added there by Jelmer Ypma. This package is a fully
 functioning, updated, and expanded version of the initial example by
 Julien Chiquet at <https://github.com/jchiquet/RcppArmadilloNLoptExample>
 also containing a large earlier pull request of mine.
	"""
	
	cran = "RcppNLoptExample" 

	version("0.0.1", md5="2127450f400f21c69fe30b3d24d5eb71")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nloptr@1.2:", type=("build", "run"))

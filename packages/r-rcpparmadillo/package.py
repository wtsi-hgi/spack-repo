# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcpparmadillo(RPackage):
	"""'Rcpp' Integration for the 'Armadillo' Templated Linear Algebra Library.

	'Armadillo' is a templated C++ linear algebra library (by Conrad;
	Sanderson) that aims towards a good balance between speed and ease of; use.
	Integer, floating point and complex numbers are supported, as; well as a
	subset of trigonometric and statistics functions. Various; matrix
	decompositions are provided through optional integration with; LAPACK and
	ATLAS libraries.  The 'RcppArmadillo' package includes the; header files
	from the templated 'Armadillo' library. Thus users do; not need to install
	'Armadillo' itself in order to use; 'RcppArmadillo'. From release 7.800.0
	on, 'Armadillo' is licensed; under Apache License 2; previous releases were
	under licensed as MPL; 2.0 from version 3.800.0 onwards and LGPL-3 prior to
	that"""

	cran = "RcppArmadillo"

	version("0.12.8.1.0", md5="96c4b6e4e870ec1a3ec02cdc47bf2000")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

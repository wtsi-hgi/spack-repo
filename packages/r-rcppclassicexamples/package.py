# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppclassicexamples(RPackage):
	"""Examples using 'RcppClassic' to Interface R and C++

	The 'Rcpp' package contains a C++ library that facilitates the
 integration of R and C++ in various ways via a rich API. This API was
 preceded by an earlier version which has been deprecated since 2010 (but is
 still supported to provide backwards compatibility in the package
 'RcppClassic').  This package 'RcppClassicExamples' provides usage examples for
 the older, deprecated API. There is also a corresponding package
 'RcppExamples' with examples for the newer, current API which we
 strongly recommend as the basis for all new development.
	"""
	
	homepage = "https://github.com/eddelbuettel/rcppclassicexamples"
	cran = "RcppClassicExamples" 

	version("0.1.3", md5="30ef1003ee8ed05c0c1f740511b6ec80")

	depends_on("r@2.15.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppclassic", type=("build", "run"))

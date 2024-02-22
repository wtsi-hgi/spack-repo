# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppexamples(RPackage):
	"""Examples using 'Rcpp' to Interface R and C++

	Examples for Seamless R and C++ integration
 The 'Rcpp' package contains a C++ library that facilitates the integration of
 R and C++ in various ways. This package provides some usage examples.
 Note that the documentation in this package currently does not cover all the
 features in the package. The site <http://gallery.rcpp.org> regroups a large
 number of examples for 'Rcpp'.
	"""
	
	homepage = "http://dirk.eddelbuettel.com/code/rcpp.examples.html"
	cran = "RcppExamples" 

	version("0.1.9", md5="0a25c3f042107b72dff4e8112558eaee")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

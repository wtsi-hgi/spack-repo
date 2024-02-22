# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcpp(RPackage):
	"""Seamless R and C++ Integration.

	The 'Rcpp' package provides R functions as well as C++ classes which; offer
	a seamless integration of R and C++. Many R data types and objects can be;
	mapped back and forth to C++ equivalents which facilitates both writing of
	new; code as well as easier integration of third-party libraries.
	Documentation; about 'Rcpp' is provided by several vignettes included in
	this package, via the; 'Rcpp Gallery' site at <https://gallery.rcpp.org>,
	the paper by Eddelbuettel and; Francois (2011,
	<doi:10.18637/jss.v040.i08>), the book by Eddelbuettel (2013,;
	<doi:10.1007/978-1-4614-6868-4>) and the paper by Eddelbuettel and Balamuta
	(2018,; <doi:10.1080/00031305.2017.1375990>); see 'citation("Rcpp")' for
	details."""

	cran = "Rcpp"

	version("1.0.12", md5="85d8f0c330b934bc8f498be40185a315")


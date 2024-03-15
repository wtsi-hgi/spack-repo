# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppcctz(RPackage):
	"""'Rcpp' Bindings for the 'CCTZ' Library.

	'Rcpp' Access to the 'CCTZ' timezone library is provided. 'CCTZ' is a C++
	library for translating between absolute and civil times using the rules of
	a time zone. The 'CCTZ' source code, released under the Apache 2.0 License,
	is included in this package. See <https://github.com/google/cctz> for more
	details."""

	cran = "RcppCCTZ"

	version("0.2.12", md5="849d052538ac2aaefefc596ba373a4ed")

	depends_on("r-rcpp", type=("build", "run"))

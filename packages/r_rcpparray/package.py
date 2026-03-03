# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcpparray(RPackage):
	"""'Rcpp' Meets 'C++' Arrays

	Interoperability between 'Rcpp' and the 'C++11' array and tuple
    types. Linking to this package allows fixed-length 'std::array' objects to
    be converted to and from equivalent R vectors, and 'std::tuple' objects
    converted to lists, via the as() and wrap() functions. There is also
    experimental support for 'std::span' from 'C++20'.
	"""
	
	homepage = "https://github.com/jonclayden/RcppArray"
	cran = "RcppArray" 

	version("0.3.0", md5="e8ba1ef6e89d06118dc1a0c092c50f86")

	depends_on("r-rcpp", type=("build", "run"))

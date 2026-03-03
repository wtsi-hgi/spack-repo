# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppfastfloat(RPackage):
	"""'Rcpp' Bindings for the 'fast_float' Header-Only Library for
Number Parsing

	Converting ascii text into (floating-point) numeric values is a
 very common problem. The 'fast_float' header-only C++ library by Daniel Lemire
 does it very well and very fast at up to or over to 1 gigabyte per second as
 described in more detail in <arXiv:2101.11408>. 'fast_float' is licensed under
 the Apache 2.0 license and provided here for use by other R packages via a simple
 'LinkingTo:' statement.
	"""
	
	homepage = "https://github.com/eddelbuettel/rcppfastfloat/"
	cran = "RcppFastFloat" 

	version("0.0.4", md5="c6976ed438f7e090994fc9f9fd0810a7")

	depends_on("r-rcpp", type=("build", "run"))

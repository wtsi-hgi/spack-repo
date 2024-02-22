# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppclassic(RPackage):
	"""Deprecated 'classic' 'Rcpp' 'API'

	The 'RcppClassic' package provides a deprecated C++ library which
 facilitates the integration of R and C++. New projects should use the new 'Rcpp'
 'API' in the 'Rcpp' package.
	"""
	
	homepage = "https://github.com/eddelbuettel/rcppclassic"
	cran = "RcppClassic" 

	version("0.9.13", md5="b933e13fa9f1e8b8d601c699c74c484c")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

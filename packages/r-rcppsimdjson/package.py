# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppsimdjson(RPackage):
	"""'Rcpp' Bindings for the 'simdjson' Header-Only Library for
'JSON' Parsing

	The 'JSON' format is ubiquitous for data interchange, and the
 'simdjson' library written by Daniel Lemire (and many contributors) provides
 a high-performance parser for these files which by relying on parallel 'SIMD'
 instruction manages to parse these files as faster than disk speed. See the
 <arXiv:1902.08318> paper for more details about 'simdjson'.  This package
 parses 'JSON' from string, file, or remote URLs under a variety of settings.
	"""
	
	homepage = "https://github.com/eddelbuettel/rcppsimdjson/"
	cran = "RcppSimdJson" 

	version("0.1.11", md5="4a86688d6331042c6874de6a595ebc88")

	depends_on("r-rcpp", type=("build", "run"))

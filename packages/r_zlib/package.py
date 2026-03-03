# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZlib(RPackage):
	"""Compression and Decompression

	The 'zlib' package for R aims to offer an R-based equivalent of 'Python's' built-in 'zlib' module for data compression and decompression. This package provides a suite of functions for working with 'zlib' compression, including utilities for compressing and decompressing data streams, manipulating compressed files, and working with 'gzip', 'zlib', and 'deflate' formats.
	"""
	
	homepage = "https://github.com/sgeist-ionos/R-zlib"
	cran = "zlib" 

	version("1.0.3", md5="3a6b28fec504f984098746ff0beb5bce")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))

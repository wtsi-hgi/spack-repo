# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcpphnsw(RPackage):
	"""'Rcpp' Bindings for 'hnswlib', a Library for Approximate
	NearestNeighbors.

	'Hnswlib' is a C++ library for Approximate Nearest Neighbors. This ;
	package provides a minimal R interface by relying on the 'Rcpp' package.
	See ; <https://github.com/nmslib/hnswlib> for more on 'hnswlib'. 'hnswlib'
	is ; released under Version 2.0 of the Apache License."""

	cran = "RcppHNSW"
	version("0.4.1", sha256="4f0082154f77dcb7756d41cdbfe0f58316431b9027081321a27942f319097c74")
	version("0.3.0", sha256="a0eb4eea65e28ba31e8306a1856f7e617a192bd448b148f88abe99181cbde007")
	version("0.1.0", sha256="75a54c30953845dec685764c7b3b4cd7315197c91aef4ab3b4eb0a6293010a95")
	version("0.6.0", md5="80b093e0f221d6aebcc9b17d090df4ae")

	depends_on("r-rcpp", type=("build", "run"))

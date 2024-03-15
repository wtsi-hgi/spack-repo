# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
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

	version("0.6.0", md5="80b093e0f221d6aebcc9b17d090df4ae")

	depends_on("r-rcpp", type=("build", "run"))

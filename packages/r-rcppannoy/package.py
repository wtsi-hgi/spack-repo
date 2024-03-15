# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppannoy(RPackage):
	"""'Rcpp' Bindings for 'Annoy', a Library for Approximate Nearest
	Neighbors.

	'Annoy' is a small C++ library for Approximate Nearest Neighbors written
	for efficient memory usage as well an ability to load from / save to disk.
	This package provides an R interface by relying on the 'Rcpp' package,
	exposing the same interface as the original Python wrapper to 'Annoy'. See
	<https://github.com/spotify/annoy> for more on 'Annoy'. 'Annoy' is released
	under Version 2.0 of the Apache License. Also included is a small Windows
	port of 'mmap' which is released under the MIT license."""

	cran = "RcppAnnoy"

	version("0.0.22", md5="8ae334c4634f6fdbc066f6a0e93dcb95")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

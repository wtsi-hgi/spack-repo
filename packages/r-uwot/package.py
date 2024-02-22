# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUwot(RPackage):
	"""The Uniform Manifold Approximation and Projection (UMAP) Method for
	Dimensionality Reduction.

	An implementation of the Uniform Manifold Approximation and Projection
	dimensionality reduction by McInnes et al. (2018) <arXiv:1802.03426>. It
	also provides means to transform new data and to carry out supervised
	dimensionality reduction. An implementation of the related LargeVis method
	of Tang et al. (2016) <arXiv:1602.00370> is also provided. This is a
	complete re-implementation in R (and C++, via the 'Rcpp' package): no
	Python installation is required. See the uwot website
	(<https://github.com/jlmelville/uwot>) for more documentation and
	examples."""

	cran = "uwot"

	version("0.1.16", md5="bc3f6277a5ef9c657baa0215964c910d")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-rcppannoy", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-dqrng", type=("build", "run"))

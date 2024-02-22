# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhilentropy(RPackage):
	"""Similarity and Distance Quantification Between Probability Functions.

	Computes 46 optimized distance and similarity measures for comparing
	probability functions (Drost (2018) <doi:10.21105/joss.00765>). These
	comparisons between probability functions have their foundations in a broad
	range of scientific disciplines from mathematics to ecology. The aim of
	this package is to provide a core framework for clustering, classification,
	statistical inference, goodness-of-fit, non-parametric statistics,
	information theory, and machine learning tasks that are based on comparing
	univariate or multivariate probability functions."""

	cran = "philentropy"

	version("0.8.0", md5="17ea7ce894ebdc0c681748ee65dafdc7")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-poorman", type=("build", "run"))

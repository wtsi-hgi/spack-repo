# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMclust(RPackage):
	"""Gaussian Mixture Modelling for Model-Based Clustering, Classification,
	and Density Estimation.

	Gaussian finite mixture models fitted via EM algorithm for model-based
	clustering, classification, and density estimation, including Bayesian
	regularization, dimension reduction for visualisation, and resampling-based
	inference."""

	cran = "mclust"

	license("GPL-2.0-or-later")

	version("6.1", md5="e07e481162d30f29d2c815050264ddd4")

	depends_on("r@3:", type=("build", "run"))

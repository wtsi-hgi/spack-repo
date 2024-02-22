# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
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

	version("6.0.1", md5="f26d75021befc4ce52ca46ad3873bd20")

	depends_on("r@3:", type=("build", "run"))

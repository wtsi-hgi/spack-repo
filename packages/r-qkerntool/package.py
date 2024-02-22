# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQkerntool(RPackage):
	"""Q-Kernel-Based and Conditionally Negative Definite Kernel-Based
Machine Learning Tools

	Nonlinear machine learning tool for classification, clustering
        and dimensionality reduction. It integrates 12 q-kernel functions and
        15 conditional negative definite kernel functions and includes the 
        q-kernel and conditional negative definite kernel version of
        density-based spatial clustering of applications with noise,
        spectral clustering, generalized discriminant analysis, principal
        component analysis, multidimensional scaling, locally linear embedding,
        sammon's mapping and t-Distributed stochastic neighbor embedding.
	"""
	
	cran = "qkerntool" 

	version("1.19", md5="25d70e185394e2d8ee1445b0a0471b5b")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))

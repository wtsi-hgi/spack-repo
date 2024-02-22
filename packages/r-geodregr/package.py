# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeodregr(RPackage):
	"""Geodesic Regression

	Provides a gradient descent algorithm to find a geodesic relationship between real-valued independent variables and a manifold-valued dependent variable (i.e. geodesic regression). Available manifolds are Euclidean space, the sphere, hyperbolic space, and Kendall's 2-dimensional shape space. Besides the standard least-squares loss, the least absolute deviations, Huber, and Tukey biweight loss functions can also be used to perform robust geodesic regression. Functions to help choose appropriate cutoff parameters to maintain high efficiency for the Huber and Tukey biweight estimators are included, as are functions for generating random tangent vectors from the Riemannian normal distributions on the sphere and hyperbolic space. The n-sphere is a n-dimensional manifold: we represent it as a sphere of radius 1 and center 0 embedded in (n+1)-dimensional space. Using the hyperboloid model of hyperbolic space, n-dimensional hyperbolic space is embedded in (n+1)-dimensional Minkowski space as the upper sheet of a hyperboloid of two sheets. Kendall's 2D shape space with K landmarks is of real dimension 2K-4; preshapes are represented as complex K-vectors with mean 0 and magnitude 1. Details are described in Shin, H.-Y. and Oh, H.-S. (2020) <arXiv:2007.04518>. Also see Fletcher, P. T. (2013) <doi:10.1007/s11263-012-0591-y>.
	"""
	
	homepage = "https://github.com/hayoungshin1/GeodRegr"
	cran = "GeodRegr" 

	version("0.2.0", md5="18e6e9a5d9a8009f26e2a6840afa7517")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass@7.3.51.6:", type=("build", "run"))
	depends_on("r-zipfr@0.6.66:", type=("build", "run"))

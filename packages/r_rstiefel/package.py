# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstiefel(RPackage):
	"""Random Orthonormal Matrix Generation and Optimization on the
Stiefel Manifold

	Simulation of random orthonormal matrices from linear and quadratic exponential family distributions on the Stiefel manifold. The most general type of distribution covered is the matrix-variate  Bingham-von Mises-Fisher distribution. Most of the simulation methods are presented in Hoff(2009) "Simulation of the Matrix Bingham-von Mises-Fisher Distribution, With Applications to Multivariate and Relational Data" <doi:10.1198/jcgs.2009.07177>. The package also includes functions for optimization on the Stiefel manifold based on algorithms described in Wen and Yin (2013) "A feasible method for optimization with orthogonality constraints" <doi:10.1007/s10107-012-0584-1>. 
	"""
	
	cran = "rstiefel" 

	version("1.0.1", md5="164d897eb3b9a66feaa8aa31926a9e15")

	depends_on("r@2.10:", type=("build", "run"))

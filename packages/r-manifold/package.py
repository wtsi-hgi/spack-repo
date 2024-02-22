# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManifold(RPackage):
	"""Operations for Riemannian Manifolds

	Implements operations for Riemannian manifolds, e.g., geodesic distance, Riemannian metric, exponential and logarithm maps, etc. Also incorporates random object generator on the manifolds. See Dai, Lin, and Müller (2021) <doi:10.1111/biom.13385>.
	"""
	
	cran = "manifold" 

	version("0.1.1", md5="b8aedc20e7e8d9d565891e9ea48ea2d3")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

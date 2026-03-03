# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigqf(RPackage):
	"""Quadratic Forms in Large Matrices

	A computationally-efficient leading-eigenvalue approximation to tail probabilities and quantiles of large quadratic forms, in particular for the Sequence Kernel Association Test (SKAT) used in genomics <doi:10.1002/gepi.22136>. Also provides stochastic singular value decomposition for dense or sparse matrices.
	"""
	
	homepage = "https://github.com/tslumley/bigQF"
	cran = "bigQF" 

	version("1.6", md5="5c9d534e528c09cdace1b43606dfff1a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-svd", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-coxme", type=("build", "run"))

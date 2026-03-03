# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdbod(RPackage):
	"""Local Density-Based Outlier Detection

	Flexible procedures to compute local density-based outlier scores for ranking outliers.
  Both exact and approximate nearest neighbor search can be implemented, while also accommodating
  multiple neighborhood sizes and four different local density-based methods. It allows for
  referencing a random subsample of the input data or a user specified reference data set
  to compute outlier scores against, so both unsupervised and semi-supervised outlier
  detection can be implemented.
	"""
	
	homepage = "https://github.com/kwilliams83/ldbod"
	cran = "ldbod" 

	version("0.1.2", md5="acc19a6dcdd2d8134179f0a5c48f32a0")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))

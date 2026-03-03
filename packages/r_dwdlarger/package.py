# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDwdlarger(RPackage):
	"""Fast Algorithms for Large Scale Generalized Distance Weighted
Discrimination

	Solving large scale distance weighted discrimination.
  The main algorithm is a symmetric Gauss-Seidel based alternating direction method of multipliers (ADMM) method. See Lam, X.Y., Marron, J.S., Sun, D.F., and Toh, K.C. (2018) <arXiv:1604.05473> for more details.
	"""
	
	homepage = "https://arxiv.org/pdf/1604.05473.pdf"
	cran = "DWDLargeR" 

	version("0.1-0", md5="b0c2b30967fca01a3a2c76f1a7e6ba02")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))

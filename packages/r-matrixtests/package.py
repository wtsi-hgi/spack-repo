# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixtests(RPackage):
	"""Fast Statistical Hypothesis Tests on Rows and Columns of
Matrices

	Functions to perform fast statistical hypothesis tests on rows/columns of matrices.
  The main goals are: 1) speed via vectorization, 2) output that is detailed and easy to use,
  3) compatibility with tests implemented in R (like those available in the 'stats' package).
	"""
	
	homepage = "https://github.com/karoliskoncevicius/matrixTests"
	cran = "matrixTests" 

	version("0.2.3", md5="1da89222ad89baef2d138cf93713b3b5")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))

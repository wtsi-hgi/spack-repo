# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatlib(RPackage):
	"""Matrix Functions for Teaching and Learning Linear Algebra and
Multivariate Statistics

	A collection of matrix functions for teaching and learning matrix
    linear algebra as used in multivariate statistical methods. These functions are
    mainly for tutorial purposes in learning matrix algebra ideas using R. In some
    cases, functions are provided for concepts available elsewhere in R, but where
    the function call or name is not obvious. In other cases, functions are provided
    to show or demonstrate an algorithm. In addition, a collection of functions are
    provided for drawing vector diagrams in 2D and 3D.
	"""
	
	homepage = "https://github.com/friendly/matlib"
	cran = "matlib" 

	version("0.9.6", md5="fb97455d2346984686b57bd4d929fcea")

	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))

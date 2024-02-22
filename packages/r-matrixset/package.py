# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixset(RPackage):
	"""Creating, Manipulating and Annotating Matrix Ensemble

	Creates an object that stores a matrix ensemble, matrices
  that share the same common properties, where rows and columns can be
  annotated. Matrices must have the same dimension and dimnames. Operators to
  manipulate these objects are provided as well as mechanisms to apply
  functions to these objects.
	"""
	
	homepage = "https://github.com/pascalcroteau/matrixset"
	cran = "matrixset" 

	version("0.3.0", md5="e5b50a1f3c0732d148e1715a76f31da6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))

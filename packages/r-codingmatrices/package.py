# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodingmatrices(RPackage):
	"""Alternative Factor Coding Matrices for Linear Model Formulae

	A collection of coding functions as alternatives to the standard
    functions in the stats package, which have names starting with 'contr.'.  Their
    main advantage is that they provide a consistent method for defining marginal
    effects in factorial models.  In a simple one-way ANOVA model the
    intercept term is always the simple average of the class means.
	"""
	
	cran = "codingMatrices" 

	version("0.4.0", md5="b7d15a0ce93cab8e8fb032ef8f4bc0e3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-fractional", type=("build", "run"))

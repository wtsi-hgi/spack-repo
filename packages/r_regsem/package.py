# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegsem(RPackage):
	"""Regularized Structural Equation Modeling

	Uses both ridge and lasso penalties (and extensions) to penalize
    specific parameters in structural equation models. The package offers additional
    cost functions, cross validation, and other extensions beyond traditional structural
    equation models. Also contains a function to perform exploratory mediation (XMed). 
	"""
	
	homepage = "https://github.com/Rjacobucci/regsem/"
	cran = "regsem" 

	version("1.9.5", md5="c248f10f794c10229eba611f3e252dd4")

	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

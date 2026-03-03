# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparser(RPackage):
	"""Variable Selection under Ranked Sparsity Principles for
Interactions and Polynomials

	
    An implementation of ranked sparsity methods, including
    penalized regression methods such as the sparsity-ranked lasso, its
    non-convex alternatives, and elastic net, as well as the sparsity-ranked
    Bayesian Information Criterion. As described in Peterson and
    Cavanaugh (2022) <doi:10.1007/s10182-021-00431-7>, ranked
    sparsity is a philosophy with methods primarily useful for
    variable selection in the presence of prior informational
    asymmetry, which occurs in the context of trying to perform variable
    selection in the presence of interactions and/or polynomials. Ultimately,
    this package attempts to facilitate dealing with cumbersome interactions
    and polynomials while not avoiding them entirely. Typically, models
    selected under ranked sparsity principles will also be more transparent,
    having fewer falsely selected interactions and polynomials than other
    methods.
	"""
	
	homepage = "https://petersonr.github.io/sparseR/"
	cran = "sparseR" 

	version("0.2.3", md5="684e757f976b7fffbfa0377b660c2a3e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-recipes@1:", type=("build", "run"))

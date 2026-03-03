# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFungible(RPackage):
	"""Psychometric Functions from the Waller Lab

	Computes fungible coefficients and Monte Carlo data. Underlying theory for these functions is described in the following publications:
    Waller, N. (2008). Fungible Weights in Multiple Regression. Psychometrika, 73(4), 691-703, <DOI:10.1007/s11336-008-9066-z>.
    Waller, N. & Jones, J. (2009). Locating the Extrema of Fungible Regression Weights.
    Psychometrika, 74(4), 589-602, <DOI:10.1007/s11336-008-9087-7>.
    Waller, N. G. (2016). Fungible Correlation Matrices:
    A Method for Generating Nonsingular, Singular, and Improper Correlation Matrices for
    Monte Carlo Research. Multivariate Behavioral Research, 51(4), 554-568.
    Jones, J. A. & Waller, N. G. (2015). The normal-theory and asymptotic distribution-free (ADF)
    covariance matrix of standardized regression coefficients: theoretical extensions
    and finite sample behavior. Psychometrika, 80, 365-378, <DOI:10.1007/s11336-013-9380-y>.
    Waller, N. G.  (2018).  Direct Schmid-Leiman transformations and rank-deficient loadings matrices.  Psychometrika, 83, 858-870. <DOI:10.1007/s11336-017-9599-0>.
	"""
	
	cran = "fungible" 

	version("2.4.4", md5="c08fba8139bbbe9a68eeb360f2f422b9")
	version("2.4.3", md5="d0f5e47d9df00c268f932356995525e0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-crayon@1.4.1:", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-cvxr", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-ga@3.2.1:", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mbess@4.8:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
	depends_on("r-rcsdp", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-sem@3.1.11:", type=("build", "run"))

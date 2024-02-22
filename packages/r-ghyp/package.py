# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGhyp(RPackage):
	"""Generalized Hyperbolic Distribution and Its Special Cases

	Detailed functionality for working
        with the univariate and multivariate Generalized Hyperbolic
        distribution and its special cases (Hyperbolic (hyp), Normal
        Inverse Gaussian (NIG), Variance Gamma (VG), skewed Student-t
        and Gaussian distribution). Especially, it contains fitting
        procedures, an AIC-based model selection routine, and functions
        for the computation of density, quantile, probability, random
        variates, expected shortfall and some portfolio optimization
        and plotting routines as well as the likelihood ratio test. In
        addition, it contains the Generalized Inverse Gaussian
        distribution. See Chapter 3 of A. J. McNeil, R. Frey, and P. Embrechts. 
        Quantitative risk management: Concepts, techniques and tools. 
        Princeton University Press, Princeton (2005).
	"""
	
	cran = "ghyp" 

	version("1.6.4", md5="d78c1601f8a633b4f3faf8624da374c1")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

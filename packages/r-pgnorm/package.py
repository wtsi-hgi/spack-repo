# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPgnorm(RPackage):
	"""The p-Generalized Normal Distribution

	Evaluation of the pdf and the cdf of the univariate,
        noncentral, p-generalized normal distribution. Sampling from
        the univariate, noncentral, p-generalized normal distribution
        using either the p-generalized polar method, the p-generalized
        rejecting polar method, the Monty Python method, the Ziggurat
        method or the method of Nardon and Pianca. The package also
        includes routines for the simulation of the bivariate,
        p-generalized uniform distribution and the simulation of the
        corresponding angular distribution.
	"""
	
	cran = "pgnorm" 

	version("2.0", md5="5d1f08cd3556a80669ab2732764d9d38")


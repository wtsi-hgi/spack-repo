# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmt(RPackage):
	"""Exact Multinomial Test: Goodness-of-Fit Test for Discrete
Multivariate Data

	Goodness-of-fit tests for discrete multivariate data. It is
        tested if a given observation is likely to have occurred under
        the assumption of an ab-initio model. Monte Carlo methods are provided to
        make the package capable of solving high-dimensional problems.
	"""
	
	cran = "EMT" 

	version("1.3", md5="71a05083cda0b119a751905a1512e83f")


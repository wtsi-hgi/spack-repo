# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvequality(RPackage):
	"""Tests for the Equality of Coefficients of Variation from
Multiple Groups

	Contains functions for testing for significant differences between multiple coefficients of variation. Includes Feltz and Miller's (1996) <DOI:10.1002/(SICI)1097-0258(19960330)15:6%3C647::AID-SIM184%3E3.0.CO;2-P> asymptotic test and Krishnamoorthy and Lee's (2014) <DOI:10.1007/s00180-013-0445-2> modified signed-likelihood ratio test. See the vignette for more, including full details of citations.
	"""
	
	homepage = "https://github.com/benmarwick/cvequality"
	cran = "cvequality" 

	version("0.2.0", md5="c1dce46b614eb480e1f638f495ff9bbd")


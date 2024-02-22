# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpthedging(RPackage):
	"""Estimation of value and hedging strategy of call and put
options

	Estimation of value and hedging strategy of call and put options, based on optimal hedging and Monte Carlo method, from Chapter 3 of 'Statistical Methods for Financial Engineering', by Bruno Remillard, CRC Press, (2013).
	"""
	
	homepage = "http://www.r-project.org"
	cran = "OptHedging" 

	version("1.0", md5="306ae095575f2ff37c404da9605e4344")


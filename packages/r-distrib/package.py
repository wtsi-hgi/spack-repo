# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistrib(RPackage):
	"""Four Essential Functions for Statistical Distributions Analysis:
A New Functional Approach

	A different way for calculating pdf/pmf, cdf, quantile and random data such that the user is able to consider the name of related distribution as an argument and so easily can changed by a changing argument by user. It must be mentioned that the core and computation base of package 'DISTRIB' is package 'stats'. Although similar functions are introduced previously in package 'stats', but the package 'DISTRIB' has some special applications in some special computational programs.
	"""
	
	cran = "DISTRIB" 

	version("1.0", md5="3b752cf4bf2280099ce129648f4a43d0")


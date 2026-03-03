# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrderstats(RPackage):
	"""Efficiently Generates Random Order Statistic Variables

	All the methods in this package generate a vector of uniform order statistics using a beta distribution and use an inverse cumulative distribution function for some distribution to give a vector of random order statistic variables for some distribution. This is much more efficient than using a loop since it is directly sampling from the order statistic distribution.
	"""
	
	cran = "orderstats" 

	version("0.1.0", md5="ad80853708cf420e30228b40093dafc3")


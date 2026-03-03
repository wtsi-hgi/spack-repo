# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCba(RPackage):
	"""Clustering for Business Analytics

	Implements clustering techniques such as Proximus and Rock, utility functions for efficient computation of cross distances and data manipulation. 
	"""
	
	cran = "cba" 

	version("0.2-23", md5="9033b1aa0baa6137fe64575dfbcd4ca3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))

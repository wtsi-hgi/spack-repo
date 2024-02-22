# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtmallows(RPackage):
	"""An Extended Mallows Model and Its Hierarchical Version for
Ranked Data Aggregation

	For multiple full/partial ranking lists, R package 'ExtMallows' can (1) detect whether the input ranking lists are over-correlated, and (2) use the Mallows model or extended Mallows model to integrate the ranking lists, and (3) use hierarchical extended Mallows model for rank integration if there are groups of over-correlated ranking lists.
	"""
	
	cran = "ExtMallows" 

	version("0.1.0", md5="963d97bfe7c17124579169cbf9a0d194")

	depends_on("r@3.1:", type=("build", "run"))

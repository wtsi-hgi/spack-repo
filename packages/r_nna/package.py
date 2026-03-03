# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNna(RPackage):
	"""Nearest-Neighbor Analysis

	Calculates spatial pattern analysis using a T-square sample procedure.
  This method is based on two measures "x" and "y".
  "x" - Distance from the random point to the nearest individual.
  "y" - Distance from individual to its nearest neighbor.
  This is a methodology commonly used in phytosociology or marine benthos ecology to analyze the species' distribution (random, uniform or clumped patterns).
  Ludwig & Reynolds (1988, ISBN:0471832359).
	"""
	
	cran = "nna" 

	version("0.0.2.1", md5="369e2fea717df1abae904725fd5f40ef")

	depends_on("r@3.4:", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPermutationr(RPackage):
	"""Conduct Permutation Analysis of Variance in R

	Conduct permutation One-Way or Two-Way Analysis of Variance in R. Use different permutation types for two-way designs. 
	"""
	
	cran = "PermutationR" 

	version("0.1.0", md5="59bebc0597c89b2992876166e17dd81f")


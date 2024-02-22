# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalacs(RPackage):
	"""Calculations for All Common Subsequences

	Implements several string comparison algorithms, including calACS (count all common subsequences), lenACS (calculate the lengths of all common subsequences), and lenLCS (calculate the length of the longest common subsequence). Some algorithms differentiate between the more strict definition of subsequence, where a common subsequence cannot be separated by any other items, from its looser counterpart, where a common subsequence can be interrupted by other items. This difference is shown in the suffix of the algorithm (-Strict vs -Loose). For example, q-w is a common subsequence of q-w-e-r and q-e-w-r on the looser definition, but not on the more strict definition. calACSLoose Algorithm from Wang, H. All common subsequences (2007) IJCAI International Joint Conference on Artificial Intelligence, pp. 635-640.
	"""
	
	cran = "calACS" 

	version("2.2.2", md5="8fd36b5458f021949f7894e35abd2a52")


# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCombinatorics(RPackage):
	"""Introduction to Some Combinatorial Relations

	Determining the value of Stirling numbers of 1st kind and 2nd kind,references: Bóna,Miklós(2017,ISBN 9789813148840).
	"""
	
	cran = "combinatorics" 

	version("0.1.0", md5="0022265fef23a96dfbe4294d38d2b9b9")


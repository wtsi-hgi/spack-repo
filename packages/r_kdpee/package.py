# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKdpee(RPackage):
	"""Fast Multidimensional Entropy Estimation by k-d Partitioning

	Estimate entropy of multidimensional data set.
	"""
	
	cran = "kdpee" 

	version("1.0.0", md5="78f00cf39da18f464817d060d9091fd3")

	depends_on("r-checkmate", type=("build", "run"))

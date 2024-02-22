# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinirand(RPackage):
	"""Minimization Randomization

	Randomization schedules are generated in the schemes with k (k>=2) treatment groups and any allocation ratios by minimization algorithms.
	"""
	
	cran = "Minirand" 

	version("0.1.3", md5="2f15e2a62badfa7c76c23ea76b5c8104")


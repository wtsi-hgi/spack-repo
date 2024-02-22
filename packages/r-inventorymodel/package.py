# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInventorymodel(RPackage):
	"""Inventory Models

	Determination of the optimal policy in inventory problems from a game-theoretic perspective.
	"""
	
	cran = "Inventorymodel" 

	version("1.1.0.1", md5="bc471b31e721c7d860aa543794e10277")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-gametheoryallocation", type=("build", "run"))

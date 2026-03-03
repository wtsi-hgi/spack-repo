# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBonev(RPackage):
	"""An Improved Multiple Testing Procedure for Controlling False
Discovery Rates

	An improved multiple testing procedure for controlling false discovery rates which is developed based on the Bonferroni procedure with integrated estimates from the Benjamini-Hochberg procedure and the Storey's q-value procedure. It controls false discovery rates through controlling the expected number of false discoveries.
	"""
	
	cran = "BonEV" 

	version("1.0", md5="f1c8d72fda765f67233e7acb6785f528")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))

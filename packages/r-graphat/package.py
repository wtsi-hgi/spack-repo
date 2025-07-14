# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphat(RPackage):
	"""Graph Theoretic Association Tests

	Functions and data used in Balasubramanian, et al. (2004)
	"""
	
	bioc = "GraphAT"

	version("1.80.0", commit="0f312c7e904a518df5e06c1868504e5e80a76cc1")
	version("1.74.0", commit="e1b7615382e33547a1aa7e52d9a5d0182e359760")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))

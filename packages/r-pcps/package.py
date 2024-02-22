# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcps(RPackage):
	"""Principal Coordinates of Phylogenetic Structure

	Set of functions for analysis of Principal Coordinates of Phylogenetic Structure (PCPS).
	"""
	
	cran = "PCPS" 

	version("1.0.7", md5="8b9238f98ed30e8dbd80973110b30c81")

	depends_on("r-syncsa@1.3.4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-picante", type=("build", "run"))
	depends_on("r-phylobase", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))

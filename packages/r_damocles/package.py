# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDamocles(RPackage):
	"""Dynamic Assembly Model of Colonization, Local Extinction and
Speciation

	Simulates and computes (maximum) likelihood of a dynamical model of community assembly that takes into account phylogenetic history.
	"""
	
	cran = "DAMOCLES" 

	version("2.3", md5="a8ab7f6f0a46975f382e8abdd0952273")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-caper", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-picante", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ddd@3.4:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))

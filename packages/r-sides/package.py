# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSides(RPackage):
	"""Subgroup Identification Based on Differential Effect Search

	Provides function to apply "Subgroup Identification based on Differential Effect Search" (SIDES) method proposed by Lipkovich et al. (2011) <doi:10.1002/sim.4289>.
	"""
	
	cran = "SIDES" 

	version("1.18", md5="4dbebf15e86ecd91b9ac3aeeb9cc6c70")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-memoise@1:", type=("build", "run"))
	depends_on("r-nnet@7.3.12:", type=("build", "run"))
	depends_on("r-multicool@0.1.9:", type=("build", "run"))
	depends_on("r-survival@2.37.7:", type=("build", "run"))
	depends_on("r-doparallel@1.0.10:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

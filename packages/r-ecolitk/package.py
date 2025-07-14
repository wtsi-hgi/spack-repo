# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcolitk(RPackage):
	"""Meta-data and tools for E. coli

	Meta-data and tools to work with E. coli. The tools are mostly plotting functions to work with circular genomes. They can used with other genomes/plasmids.
	"""
	
	bioc = "ecolitk"

	version("1.80.0", commit="46c4636daff2490302ab5ee58357af77908165d6")
	version("1.74.0", commit="acc30290adf909d3a094818195ae03262ca0ff73")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

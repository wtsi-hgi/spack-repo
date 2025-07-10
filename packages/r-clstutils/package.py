# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClstutils(RPackage):
	"""Tools for performing taxonomic assignment

	Tools for performing taxonomic assignment based on phylogeny using pplacer and clst.
	"""
	
	bioc = "clstutils" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/clstutils_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/clstutils/clstutils_1.50.0.tar.gz"]

	version("1.50.0", sha256="c618db94a7359eec52c5a336b092b1524d22c29dc9677a8818fbc80a87d08172")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-clst", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))

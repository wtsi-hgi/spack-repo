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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/clstutils_1.50.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/clstutils/clstutils_1.50.0.tar.gz"]

	version("1.50.0", md5="4343490b2b05bf2e4429f2081b3a82c5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-clst", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))

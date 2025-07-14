# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenestructuretools(RPackage):
	"""Tools for spliced gene structure manipulation and analysis

	GeneStructureTools can be used to create in silico alternative splicing events, and analyse potential effects this has on functional gene products.
	"""
	
	bioc = "GeneStructureTools"

	version("1.28.0", commit="f23a47c17e99f3ae0f5a94dbbe405754ed11596e")
	version("1.22.0", commit="81b9c5ec56162e53894144abf25b951b78df1c43")

	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-bsgenome-mmusculus-ucsc-mm10", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))

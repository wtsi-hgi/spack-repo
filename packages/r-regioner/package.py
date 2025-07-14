# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegioner(RPackage):
	"""Association analysis of genomic regions based on permutation tests

	regioneR offers a statistical framework based on customizable permutation tests to assess the association between genomic region sets and other genomic features.
	"""
	
	bioc = "regioneR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/regioneR_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/regioneR/regioneR_1.34.0.tar.gz"]

    version("1.40.1", tag="RELEASE_3_21")
	version("1.34.0", sha256="32fa22d1ef19db168a017578178a61b38c4e82b4572595eed0cf3ad18e5c8fe1")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

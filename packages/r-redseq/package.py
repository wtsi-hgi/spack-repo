# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedseq(RPackage):
	"""Analysis of high-throughput sequencing data processed by restriction enzyme digestion

	The package includes functions to build restriction enzyme cut site (RECS) map, distribute mapped sequences on the map with five different approaches, find enriched/depleted RECSs for a sample, and identify differentially enriched/depleted RECSs between samples.
	"""
	
	bioc = "REDseq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/REDseq_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/REDseq/REDseq_1.48.0.tar.gz"]

	version("1.48.0", md5="f20e437ad9c48683bdaeda1825f87f85")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-bsgenome-celegans-ucsc-ce2", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-chippeakanno", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-iranges@1.13.5:", type=("build", "run"))

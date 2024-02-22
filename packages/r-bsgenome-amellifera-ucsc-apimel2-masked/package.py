# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeAmelliferaUcscApimel2Masked(RPackage):
	"""Full masked genome sequences for Apis mellifera (UCSC version apiMel2)

	Full genome sequences for Apis mellifera (Honey Bee) as provided by UCSC (apiMel2, Jan. 2005) and stored in Biostrings objects. The sequences are the same as in BSgenome.Amellifera.UCSC.apiMel2, except that each of them has the 3 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), and (3) the mask of repeats from RepeatMasker (RM mask). Only the AGAPS and AMB masks are "active" by default.
	"""
	
	bioc = "BSgenome.Amellifera.UCSC.apiMel2.masked" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Amellifera.UCSC.apiMel2.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Amellifera.UCSC.apiMel2.masked/BSgenome.Amellifera.UCSC.apiMel2.masked_1.3.99.tar.gz"]

	version("1.3.99", md5="e7a7ff8cfce8e239b22116855456f23d")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-amellifera-ucsc-apimel2", type=("build", "run"))

	# annotation
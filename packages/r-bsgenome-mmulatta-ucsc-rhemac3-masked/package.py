# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMmulattaUcscRhemac3Masked(RPackage):
	"""Full masked genome sequences for Macaca mulatta (UCSC version rheMac3)

	Full genome sequences for Macaca mulatta (Rhesus) as provided by UCSC (rheMac3, Oct. 2010) and stored in Biostrings objects. The sequences are the same as in BSgenome.Mmulatta.UCSC.rheMac3, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.
	"""
	
	bioc = "BSgenome.Mmulatta.UCSC.rheMac3.masked" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmulatta.UCSC.rheMac3.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Mmulatta.UCSC.rheMac3.masked/BSgenome.Mmulatta.UCSC.rheMac3.masked_1.3.99.tar.gz"]

	version("1.3.99", md5="94f8714865655d3144e14f6fc5c24e76")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-mmulatta-ucsc-rhemac3", type=("build", "run"))

	# annotation
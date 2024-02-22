# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMmulattaUcscRhemac2Masked(RPackage):
	"""Full masked genome sequences for Macaca mulatta (UCSC version rheMac2)

	Full genome sequences for Macaca mulatta (Rhesus) as provided by UCSC (rheMac2, Jan. 2006) and stored in Biostrings objects. The sequences are the same as in BSgenome.Mmulatta.UCSC.rheMac2, except that each of them has the 4 following masks on top: (1) the mask of assembly gaps (AGAPS mask), (2) the mask of intra-contig ambiguities (AMB mask), (3) the mask of repeats from RepeatMasker (RM mask), and (4) the mask of repeats from Tandem Repeats Finder (TRF mask). Only the AGAPS and AMB masks are "active" by default.  NOTE: In most assemblies available at UCSC, Tandem Repeats Finder repeats were filtered to retain only the repeats with period <= 12.  However, the filtering was omitted for this assembly, so the TRF masks contain all Tandem Repeats Finder results.
	"""
	
	bioc = "BSgenome.Mmulatta.UCSC.rheMac2.masked" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Mmulatta.UCSC.rheMac2.masked_1.3.99.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Mmulatta.UCSC.rheMac2.masked/BSgenome.Mmulatta.UCSC.rheMac2.masked_1.3.99.tar.gz"]

	version("1.3.99", md5="7602d86b68df7e4c8d336fede4090a62")

	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-mmulatta-ucsc-rhemac2", type=("build", "run"))

	# annotation
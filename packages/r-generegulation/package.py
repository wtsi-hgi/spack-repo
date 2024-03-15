# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneregulation(RPackage):
	"""Finding Candidate Binding Sites for Known Transcription Factors via Sequence Matching

	The binding of transcription factor proteins (TFs) to DNA promoter regions upstream of gene transcription start sites (TSSs) is one of the most important mechanisms by which gene expression, and thus many cellular processes, are controlled. Though in recent years many new kinds of data have become available for identifying transcription factor binding sites (TFBSs) -- ChIP-seq and DNase I hypersensitivity regions among them -- sequence matching continues to play an important role. In this workflow we demonstrate Bioconductor techniques for finding candidate TF binding sites in DNA sequence using the model organism Saccharomyces cerevisiae.  The methods demonstrated here apply equally well to other organisms.
	"""
	
	homepage = "https://www.bioconductor.org/help/workflows/generegulation/"
	bioc = "generegulation" 
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/generegulation_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/generegulation/generegulation_1.26.0.tar.gz"]

	version("1.26.0", md5="7e2383f24874237d8e5734515d61adcf")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-bsgenome-scerevisiae-ucsc-saccer3", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-motifdb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-txdb-scerevisiae-ucsc-saccer3-sgdgene", type=("build", "run"))
	depends_on("r-motifstack", type=("build", "run"))
	depends_on("r-org-sc-sgd-db", type=("build", "run"))
	depends_on("r-seqlogo", type=("build", "run"))

	# workflow
# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChippeakanno(RPackage):
	"""Batch annotation of the peaks identified from either ChIP-seq, ChIP-chip experiments or any experiments resulted in large number of chromosome ranges

	The package includes functions to retrieve the sequences around the peak, obtain enriched Gene Ontology (GO) terms, find the nearest gene, exon, miRNA or custom features such as most conserved elements and other transcription factor binding sites supplied by users. Starting 2.0.5, new functions have been added for finding the peaks with bi-directional promoters with summary statistics (peaksNearBDP), for summarizing the occurrence of motifs in peaks (summarizePatternInPeaks) and for adding other IDs to annotated peaks or enrichedGO (addGeneIDs). This package leverages the biomaRt, IRanges, Biostrings, BSgenome, GO.db, multtest and stat packages.
	"""
	
	bioc = "ChIPpeakAnno" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ChIPpeakAnno_3.36.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ChIPpeakAnno/ChIPpeakAnno_3.36.1.tar.gz"]

    version("3.42.0", tag="RELEASE_3_21")
	version("3.36.1", sha256="74a309929f41e74b5d8ea0366b233185ea0d982542fe78ebd8292ab45149afca")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-iranges@2.13.12:", type=("build", "run"))
	depends_on("r-genomicranges@1.31.8:", type=("build", "run"))
	depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocgenerics@0.1:", type=("build", "run"))
	depends_on("r-biostrings@2.47.6:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-interactionset", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-regioner", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))

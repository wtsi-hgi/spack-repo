# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgseq(RPackage):
	"""Splice event prediction and quantification from RNA-seq data

	SGSeq is a software package for analyzing splice events from RNA-seq data. Input data are RNA-seq reads mapped to a reference genome in BAM format. Genes are represented as a splice graph, which can be obtained from existing annotation or predicted from the mapped sequence reads. Splice events are identified from the graph and are quantified locally using structurally compatible reads at the start or end of each splice variant. The software includes functions for splice event prediction, quantification, visualization and interpretation.
	"""
	
	bioc = "SGSeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SGSeq_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SGSeq/SGSeq_1.36.0.tar.gz"]

	version("1.36.0", md5="874492401a4a17bf0836f9fa011f459a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-iranges@2.13.15:", type=("build", "run"))
	depends_on("r-genomicranges@1.31.10:", type=("build", "run"))
	depends_on("r-rsamtools@1.31.2:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocgenerics@0.31.5:", type=("build", "run"))
	depends_on("r-biostrings@2.47.6:", type=("build", "run"))
	depends_on("r-genomicalignments@1.15.7:", type=("build", "run"))
	depends_on("r-genomicfeatures@1.31.5:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
	depends_on("r-s4vectors@0.23.19:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rtracklayer@1.39.7:", type=("build", "run"))

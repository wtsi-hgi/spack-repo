# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonalisa(RPackage):
	"""Binned Motif Enrichment Analysis and Visualization

	Useful functions to work with sequence motifs in the analysis of genomics data. These include methods to annotate genomic regions or sequences with predicted motif hits and to identify motifs that drive observed changes in accessibility or expression. Functions to produce informative visualizations of the obtained results are also provided.
	"""
	
	homepage = "https://github.com/fmicompbio/monaLisa"
	bioc = "monaLisa" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/monaLisa_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/monaLisa/monaLisa_1.8.0.tar.gz"]

    version("1.14.0", tag="RELEASE_3_21")
	version("1.8.0", md5="fc86eb3743fc47252a4420cd850ead9e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-tfbstools", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-stabs", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-complexheatmap@2.11.1:", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-vioplot", type=("build", "run"))

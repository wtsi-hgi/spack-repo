# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatzie(RPackage):
	"""Identification of enriched motif pairs from chromatin interaction data

	Identifies motifs that are significantly co-enriched from enhancer-promoter interaction data. While enhancer-promoter annotation is commonly used to define groups of interaction anchors, spatzie also supports co-enrichment analysis between preprocessed interaction anchors.  Supports BEDPE interaction data derived from genome-wide assays such as HiC, ChIA-PET, and HiChIP. Can also be used to look for differentially enriched motif pairs between two interaction experiments.
	"""
	
	homepage = "https://spatzie.mit.edu"
	bioc = "spatzie" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/spatzie_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/spatzie/spatzie_1.8.0.tar.gz"]

	version("1.8.0", md5="fa887a71329c75cde9ab0b1aaeb0d481")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicinteractions", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-motifmatchr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tfbstools", type=("build", "run"))

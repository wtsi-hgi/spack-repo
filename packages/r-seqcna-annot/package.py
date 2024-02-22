# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqcnaAnnot(RPackage):
	"""Annotation for the copy number analysis of deep sequencing cancer data with seqCNA

	Provides annotation on GC content, mappability and genomic features for various genomes
	"""
	
	bioc = "seqCNA.annot" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/seqCNA.annot_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/seqCNA.annot/seqCNA.annot_1.38.0.tar.gz"]

	version("1.38.0", md5="a61df6e0824d7c3c3f4c697b5bd73e30")

	depends_on("r@2.10:", type=("build", "run"))

	# experiment
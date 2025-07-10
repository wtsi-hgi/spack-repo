# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSagenhaft(RPackage):
	"""Collection of functions for reading and comparing SAGE libraries

	This package implements several functions useful for analysis of gene expression data by sequencing tags as done in SAGE (Serial Analysis of Gene Expressen) data, i.e. extraction of a SAGE library from sequence files, sequence error correction, library comparison. Sequencing error correction is implementing using an Expectation Maximization Algorithm based on a Mixture Model of tag counts.
	"""
	
	homepage = "http://www.bioinf.med.uni-goettingen.de"
	bioc = "sagenhaft" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sagenhaft_1.72.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sagenhaft/sagenhaft_1.72.0.tar.gz"]

	version("1.72.0", sha256="5b833759e7997e0218108bfd3e6fb4a540d13e630a7b8012358371c4a5588c05")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sparsem@0.73:", type=("build", "run"))

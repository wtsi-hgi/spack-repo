# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnabarcodes(RPackage):
	"""A tool for creating and analysing DNA barcodes used in Next Generation Sequencing multiplexing experiments

	The package offers a function to create DNA barcode sets capable of correcting insertion, deletion, and substitution errors. Existing barcodes can be analysed regarding their minimal, maximal and average distances between barcodes. Finally, reads that start with a (possibly mutated) barcode can be demultiplexed, i.e., assigned to their original reference barcode.
	"""
	
	bioc = "DNABarcodes" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DNABarcodes_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DNABarcodes/DNABarcodes_1.32.0.tar.gz"]

	version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="09263a219f974c60eeb384fc391a47d967eac19d6ffe81e8f77c433d4b99a48b")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))

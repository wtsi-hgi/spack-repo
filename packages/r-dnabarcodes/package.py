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

	version("1.38.0", commit="7977a34eb86bf7de7897c2e3505d7c6019558df1")
	version("1.32.0", commit="5d76e7413c7a14dba43d38a9efd134f5dffa06a8")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))

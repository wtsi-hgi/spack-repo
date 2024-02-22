# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGirafe(RPackage):
	"""Genome Intervals and Read Alignments for Functional Exploration

	The package 'girafe' deals with the genome-level representation of aligned reads from next-generation sequencing data. It contains an object class for enabling a detailed description of genome intervals with aligned reads and functions for comparing, visualising, exporting and working with such intervals and the aligned reads. As such, the package interacts with and provides a link between the packages ShortRead, IRanges and genomeIntervals.
	"""
	
	bioc = "girafe" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/girafe_1.54.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/girafe/girafe_1.54.0.tar.gz"]

	version("1.54.0", md5="4cf228e6d7f73cf97c923f1c349fb6c3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biocgenerics@0.13.8:", type=("build", "run"))
	depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
	depends_on("r-rsamtools@1.31.2:", type=("build", "run"))
	depends_on("r-intervals@0.13.1:", type=("build", "run"))
	depends_on("r-shortread@1.37.1:", type=("build", "run"))
	depends_on("r-genomeintervals@1.25.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biostrings@2.47.6:", type=("build", "run"))
	depends_on("r-iranges@2.13.12:", type=("build", "run"))

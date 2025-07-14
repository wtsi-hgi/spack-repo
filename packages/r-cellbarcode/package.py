# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellbarcode(RPackage):
	"""Cellular DNA Barcode Analysis toolkit

	The package CellBarcode performs Cellular DNA Barcode analysis. It can handle all kinds of DNA barcodes, as long as the barcode is within a single sequencing read and has a pattern that can be matched by a regular expression. code{CellBarcode} can handle barcodes with flexible lengths, with or without UMI (unique molecular identifier). This tool also can be used for pre-processing some amplicon data such as CRISPR gRNA screening, immune repertoire sequencing, and metagenome data.
	"""
	
	homepage = "https://wenjie1991.github.io/CellBarcode/"
	bioc = "CellBarcode" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CellBarcode_1.8.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CellBarcode/CellBarcode_1.8.1.tar.gz"]

	version("1.14.0", tag="RELEASE_3_21")
	version("1.8.1", sha256="9ba0c45bedd91a219a0e7dc1841b32329a5204ce0cdad95b7a36b296ff879540")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table@1.12.6:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shortread@1.48:", type=("build", "run"))
	depends_on("r-biostrings@2.58:", type=("build", "run"))
	depends_on("r-egg", type=("build", "run"))
	depends_on("r-ckmeans-1d-dp", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))

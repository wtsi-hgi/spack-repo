# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSomaticsignatures(RPackage):
	"""Somatic Signatures.

	The SomaticSignatures package identifies mutational signatures of single
	nucleotide variants (SNVs). It provides a infrastructure related to the
	methodology described in Nik-Zainal (2012, Cell), with flexibility in
	the matrix decomposition algorithms."""

	bioc = "SomaticSignatures"

	license("MIT")
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SomaticSignatures_2.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SomaticSignatures/SomaticSignatures_2.38.0.tar.gz"]

	version("2.38.0", md5="46d14334be0098323bc956bade5d5e9e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggbio", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdsfmt(RPackage):
	"""R Interface to CoreArray Genomic Data Structure (GDS) Files.

	This package provides a high-level R interface to CoreArray Genomic Data
	Structure (GDS) data files, which are portable across platforms with
	hierarchical structure to store multiple scalable array-oriented data
	sets with metadata information. It is suited for large-scale datasets,
	especially for data which are much larger than the available random-
	access memory. The gdsfmt package offers the efficient operations
	specifically designed for integers of less than 8 bits, since a diploid
	genotype, like single-nucleotide polymorphism (SNP), usually occupies
	fewer bits than a byte. Data compression and decompression are available
	with relatively efficient random access. It is also allowed to read a
	GDS file in parallel with multiple R processes supported by the package
	parallel."""

	bioc = "gdsfmt"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/gdsfmt_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/gdsfmt/gdsfmt_1.38.0.tar.gz"]

	version("1.38.0", md5="8851c188356c12f7e99488ceb4daeca8")

	depends_on("r@2.15:", type=("build", "run"))

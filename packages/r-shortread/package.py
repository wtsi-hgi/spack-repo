# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShortread(RPackage):
	"""FASTQ input and manipulation.

	This package implements sampling, iteration, and input of FASTQ files.
	The package includes functions for filtering and trimming reads, and for
	generating a quality assessment report. Data are represented as
	DNAStringSet-derived objects, and easily manipulated for a diversity of
	purposes. The package also contains legacy support for early single-end,
	ungapped alignment formats."""

	bioc = "ShortRead"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ShortRead_1.60.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ShortRead/ShortRead_1.60.0.tar.gz"]

	version("1.60.0", md5="480786b1db8f8138a7a4e8c36f9bdfc4")

	depends_on("r-biocgenerics@0.23.3:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rsamtools@1.31.2:", type=("build", "run"))
	depends_on("r-genomicalignments@1.15.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb@1.15.2:", type=("build", "run"))
	depends_on("r-genomicranges@1.31.8:", type=("build", "run"))
	depends_on("r-hwriter", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-rhtslib", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))

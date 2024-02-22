# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsamtools(RPackage):
	"""Binary alignment (BAM), FASTA, variant call (BCF), and tabix file
	import.

	This package provides an interface to the 'samtools', 'bcftools', and
	'tabix' utilities for manipulating SAM (Sequence Alignment / Map),
	FASTA, binary variant call (BCF) and compressed indexed tab-delimited
	(tabix) files."""

	bioc = "Rsamtools"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Rsamtools_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Rsamtools/Rsamtools_2.18.0.tar.gz"]

	version("2.18.0", md5="63af2a7dd2513e992fd78b26ca2b3775")

	depends_on("r-genomeinfodb@1.1.3:", type=("build", "run"))
	depends_on("r-genomicranges@1.31.8:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics@0.25.1:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rhtslib@1.99.3:", type=("build", "run"))
	depends_on("lzma", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))

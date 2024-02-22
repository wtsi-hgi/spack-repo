# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtracklayer(RPackage):
	"""R interface to genome annotation files and the UCSC genome browser.

	Extensible framework for interacting with multiple genome browsers
	(currently UCSC built-in) and manipulating annotation tracks in various
	formats (currently GFF, BED, bedGraph, BED15, WIG, BigWig and 2bit
	built-in). The user may export/import tracks to/from the supported
	browsers, as well as query and modify the browser state, such as the
	current viewport."""

	bioc = "rtracklayer"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rtracklayer_1.62.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rtracklayer/rtracklayer_1.62.0.tar.gz"]

	version("1.62.0", md5="a16a9ca02e49808b38823899860abdb6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges@1.37.2:", type=("build", "run"))
	depends_on("r-xml@1.98.0:", type=("build", "run"))
	depends_on("r-biocgenerics@0.35.3:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-genomeinfodb@1.15.2:", type=("build", "run"))
	depends_on("r-biostrings@2.47.6:", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-rcurl@1.4.2:", type=("build", "run"))
	depends_on("r-rsamtools@1.31.2:", type=("build", "run"))
	depends_on("r-genomicalignments@1.15.6:", type=("build", "run"))
	depends_on("r-biocio", type=("build", "run"))
	depends_on("r-restfulr@0.0.13:", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))

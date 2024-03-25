# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBamsignals(RPackage):
	"""Extract read count signals from bam files.

	This package allows to efficiently obtain count vectors from indexed bam
	files. It counts the number of reads in given genomic ranges and it
	computes reads profiles and coverage profiles. It also handles paired-
	end data."""

	bioc = "bamsignals"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/bamsignals_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/bamsignals/bamsignals_1.34.0.tar.gz"]

	version("1.34.0", md5="e7b42351aa9651bdf7d429a6377143f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-rhtslib@1.13.1:", type=("build", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("lzma", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))

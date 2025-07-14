# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPackfinder(RPackage):
	"""de novo Annotation of Pack-TYPE Transposable Elements

	Algorithm and tools for in silico pack-TYPE transposon discovery. Filters a given genome for properties unique to DNA transposons and provides tools for the investigation of returned matches. Sequences are input in DNAString format, and ranges are returned as a dataframe (in the format returned by as.dataframe(GRanges)).
	"""
	
	homepage = "https://github.com/jackgisby/packFinder"
	bioc = "packFinder"

	version("1.20.0", commit="7d1efefd379fe90b874dcad9b03610c12bdc1b1c")
	version("1.14.0", commit="cebb7c82eb5c79499be926cec545cb705e57d00a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-kmer", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

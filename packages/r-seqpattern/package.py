# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqpattern(RPackage):
	"""Visualising oligonucleotide patterns and motif occurrences across a set of sorted sequences

	Visualising oligonucleotide patterns and sequence motifs occurrences across a large set of sequences centred at a common reference point and sorted by a user defined feature.
	"""
	
	bioc = "seqPattern" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/seqPattern_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/seqPattern/seqPattern_1.34.0.tar.gz"]

	version("1.34.0", md5="90ef37347887673ee80f12fa953e02f3")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))

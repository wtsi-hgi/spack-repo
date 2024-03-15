# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcistargetHg19MotifdbsCisbponly500bp(RPackage):
	"""RcisTarget motif databases for human (hg19) - Subset of 4.6k motifs

	RcisTarget databases: Gene-based motif rankings and annotation to transcription factors. This package contains a subset of 4.6k motifs (cisbp motifs), scored only within 500bp upstream and the TSS. See RcisTarget tutorial to download the full databases, containing 20k motifs and search space up to 10kbp around the TSS.
	"""
	
	homepage = "http://scenic.aertslab.org"
	bioc = "RcisTarget.hg19.motifDBs.cisbpOnly.500bp" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RcisTarget.hg19.motifDBs.cisbpOnly.500bp_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RcisTarget.hg19.motifDBs.cisbpOnly.500bp/RcisTarget.hg19.motifDBs.cisbpOnly.500bp_1.22.0.tar.gz"]

	version("1.22.0", md5="b8cdbfafeb9966332876fdf9be8dbb5a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))

	# experiment
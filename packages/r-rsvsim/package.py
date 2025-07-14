# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsvsim(RPackage):
	"""RSVSim: an R/Bioconductor package for the simulation of structural variations

	RSVSim is a package for the simulation of deletions, insertions, inversion, tandem-duplications and translocations of various sizes in any genome available as FASTA-file or BSgenome data package. SV breakpoints can be placed uniformly accross the whole genome, with a bias towards repeat regions and regions of high homology (for hg19) or at user-supplied coordinates.
	"""
	
	bioc = "RSVSim"

	version("1.48.0", commit="d157a0cb41d8ce432b408d914de70581697a4599")
	version("1.42.0", commit="3cc9f3d05279a0fff47a336659cac5ce8afdd84d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))

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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RSVSim_1.42.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RSVSim/RSVSim_1.42.0.tar.gz"]

	version("1.42.0", md5="0ce59bfd8791d8b1bf0b4fa48ea37e31")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))

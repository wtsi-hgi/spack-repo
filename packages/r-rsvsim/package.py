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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RSVSim_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RSVSim/RSVSim_1.42.0.tar.gz"]

	version("1.42.0", sha256="d4e84df70b3de7e9b33d22c71ae97831f86cb08ed391e4a1d6028e36b49f317f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))

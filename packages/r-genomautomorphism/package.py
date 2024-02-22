# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomautomorphism(RPackage):
	"""Compute the automorphisms between DNA's Abelian group representations

	This is a R package to compute the automorphisms between pairwise aligned DNA sequences represented as elements from a Genomic Abelian group. In a general scenario, from genomic regions till the whole genomes from a given population (from any species or close related species) can be algebraically represented as a direct sum of cyclic groups or more specifically Abelian p-groups. Basically, we propose the representation of multiple sequence alignments of length N bp as element of a finite Abelian group created by the direct sum of homocyclic Abelian group of prime-power order.
	"""
	
	homepage = "https://github.com/genomaths/GenomAutomorphism"
	bioc = "GenomAutomorphism" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GenomAutomorphism_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GenomAutomorphism/GenomAutomorphism_1.4.0.tar.gz"]

	version("1.4.0", md5="36ebcd90b454dc7450e875730537811b")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))

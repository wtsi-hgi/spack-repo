# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJackalope(RPackage):
	"""A Swift, Versatile Phylogenomic and High-Throughput Sequencing
Simulator

	Simply and efficiently
    simulates (i) variants from reference genomes and (ii) reads from both Illumina 
    <https://www.illumina.com/>
    and Pacific Biosciences (PacBio) <https://www.pacb.com/> platforms. 
    It can either read reference genomes from FASTA files or simulate new ones.
    Genomic variants can be simulated using summary statistics, phylogenies, 
    Variant Call Format (VCF) files, and coalescent simulations—the latter of which
    can include selection, recombination, and demographic fluctuations.
    'jackalope' can simulate single, paired-end, or mate-pair Illumina reads, 
    as well as PacBio reads.
    These simulations include sequencing errors, mapping qualities, multiplexing,
    and optical/polymerase chain reaction (PCR) duplicates.
    Simulating Illumina sequencing is based on ART
    by Huang et al. (2012) <doi:10.1093/bioinformatics/btr708>.
    PacBio sequencing simulation is based on 
    SimLoRD  by Stöcker et al. (2016) <doi:10.1093/bioinformatics/btw286>.
    All outputs can be written to standard file formats.
	"""
	
	homepage = "https://github.com/lucasnell/jackalope"
	cran = "jackalope" 

	version("1.1.5", md5="7cdd86fc94e8a4d4734f8a71037aa12e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rhtslib", type=("build", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))

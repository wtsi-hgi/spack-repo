# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynmut(RPackage):
	"""SynMut: Designing Synonymously Mutated Sequences with Different Genomic Signatures

	There are increasing demands on designing virus mutants with specific dinucleotide or codon composition. This tool can take both dinucleotide preference and/or codon usage bias into account while designing mutants. It is a powerful tool for in silico designs of DNA sequence mutants.
	"""
	
	homepage = "https://github.com/Koohoko/SynMut"
	bioc = "SynMut" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SynMut_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SynMut/SynMut_1.18.0.tar.gz"]

	version("1.18.0", md5="485dd0770e2c64ad7ace9a3edf957fe8")

	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqtools(RPackage):
	"""Analysis of nucleotide, sequence and quality content on fastq files

	Analyze read length, phred scores and alphabet frequency and DNA k-mers on uncompressed and compressed fastq files.
	"""
	
	bioc = "seqTools" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/seqTools_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/seqTools/seqTools_1.36.0.tar.gz"]

	version("1.36.0", md5="be9be6eb0ee1ff4ab001720970d68da8")

	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))

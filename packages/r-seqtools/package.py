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

    version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="559031059a9315d8b0912d5334c91cb5176427e09586df400b3eeff58b9a1584")

	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))

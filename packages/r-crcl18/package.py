# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrcl18(RPackage):
	"""CRC cell line dataset

	colorectal cancer mRNA and miRNA on 18 cell lines
	"""
	
	bioc = "CRCL18" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/CRCL18_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/CRCL18/CRCL18_1.22.0.tar.gz"]

	version("1.22.0", md5="176bd921f08e717ec49e4e3eb4a5e5e5", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/CRCL18_1.22.0.tar.gz")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))


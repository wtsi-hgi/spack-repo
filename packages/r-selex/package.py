# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelex(RPackage):
	"""Functions for analyzing SELEX-seq data

	Tools for quantifying DNA binding specificities based on SELEX-seq data.
	"""
	
	homepage = "https://bussemakerlab.org/site/software/"
	bioc = "SELEX" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SELEX_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SELEX/SELEX_1.34.0.tar.gz"]

	version("1.34.0", md5="fdb39d601a2ce8c882e9a0e822ef014c")

	depends_on("r-rjava@0.5.0:", type=("build", "run"))
	depends_on("r-biostrings@2.26:", type=("build", "run"))
	depends_on("openjdk@1.5:", type=("build", "link", "run"))

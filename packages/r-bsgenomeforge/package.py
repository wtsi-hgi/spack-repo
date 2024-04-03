# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeforge(RPackage):
	"""Forge BSgenome data packages

	A set of tools to forge BSgenome data packages. Supersedes the old seed-based tools from the BSgenome software package. This package allows the user to create a BSgenome data package in one function call, simplifying the old seed-based process.
	"""
	
	homepage = "https://bioconductor.org/packages/BSgenomeForge"
	bioc = "BSgenomeForge" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BSgenomeForge_1.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BSgenomeForge/BSgenomeForge_1.2.3.tar.gz"]

	version("1.2.1", md5="7a8ad7be8dbfe9034eb38bb87bf92e31")
	version("1.2.3", md5="f6b0c95390692557860c977b1eba0f0c")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb@1.33.17:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))

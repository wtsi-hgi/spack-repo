# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdblock(RPackage):
	"""data structures for linkage disequilibrium measures in populations

	Define data structures for linkage disequilibrium measures in populations.
	"""
	
	bioc = "ldblock" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ldblock_1.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ldblock/ldblock_1.32.0.tar.gz"]

	version("1.32.0", md5="579c380a003913fde7767f15b47a6692")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-biocgenerics@0.25.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

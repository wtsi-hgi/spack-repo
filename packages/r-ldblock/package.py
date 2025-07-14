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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ldblock_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ldblock/ldblock_1.32.0.tar.gz"]

    version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="1730eb16951ce61901bd93c55a5f04d751d4d8b6b57951416242bd9912fb5db1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-biocgenerics@0.25.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

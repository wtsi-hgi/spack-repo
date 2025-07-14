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

	version("1.38.0", commit="aad2e2a707b276d482a6840937384871eab050e1")
	version("1.32.0", commit="398acc977660d9addd4ce5f8491af290470442a2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-biocgenerics@0.25.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

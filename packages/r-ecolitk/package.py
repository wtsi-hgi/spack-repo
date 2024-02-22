# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcolitk(RPackage):
	"""Meta-data and tools for E. coli

	Meta-data and tools to work with E. coli. The tools are mostly plotting functions to work with circular genomes. They can used with other genomes/plasmids.
	"""
	
	bioc = "ecolitk" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ecolitk_1.74.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ecolitk/ecolitk_1.74.0.tar.gz"]

	version("1.74.0", md5="58667dc1f403986935c98a97f2e0b9e2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

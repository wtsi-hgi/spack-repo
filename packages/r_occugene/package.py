# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROccugene(RPackage):
	"""Functions for Multinomial Occupancy Distribution

	Statistical tools for building random mutagenesis libraries for prokaryotes. The package has functions for handling the occupancy distribution for a multinomial and for estimating the number of essential genes in random transposon mutagenesis libraries.
	"""
	
	bioc = "occugene" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/occugene_1.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/occugene/occugene_1.62.0.tar.gz"]

	version("1.62.0", md5="264da1422714d735ac474b414e57a2a9")

	depends_on("r@2:", type=("build", "run"))

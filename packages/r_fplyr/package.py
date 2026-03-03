# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFplyr(RPackage):
	"""Apply Functions to Blocks of Files

	Read and process a large delimited file block by
    block. A block consists of all the contiguous rows that have the same value
    in the first field. The result can be returned as a list or a data.table,
    or even directly printed to an output file.
	"""
	
	homepage = "https://github.com/fmarotta/fplyr"
	cran = "fplyr" 

	version("1.3.0", md5="bd871752b6b8429274df05500f6cd75f")

	depends_on("r-data-table@1.1.4:", type=("build", "run"))
	depends_on("r-iotools@0.2.5:", type=("build", "run"))

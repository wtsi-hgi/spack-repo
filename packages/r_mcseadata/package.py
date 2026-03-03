# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcseadata(RPackage):
	"""Data package for mCSEA package

	Data objects necessary to some mCSEA package functions. There are also example data objects to illustrate mCSEA package functionality.
	"""
	
	bioc = "mCSEAdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/mCSEAdata_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/mCSEAdata/mCSEAdata_1.22.0.tar.gz"]

	version("1.22.0", md5="11f8150e223a0e8d8fa5b9b8dedaa374")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))


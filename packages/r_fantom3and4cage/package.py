# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFantom3and4cage(RPackage):
	"""CAGE data from FANTOM3 and FANTOM4 projects

	CAGE (Cap Analysis Gene Expression) data from FANTOM3 and FANTOM4 projects produced by RIKEN Omics Science Center.
	"""
	
	bioc = "FANTOM3and4CAGE" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/FANTOM3and4CAGE_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/FANTOM3and4CAGE/FANTOM3and4CAGE_1.38.0.tar.gz"]

	version("1.38.0", md5="5d964e7a085d6a7b00e2b2215b765861")

	depends_on("r@2.15:", type=("build", "run"))


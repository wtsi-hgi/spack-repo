# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnadata(RPackage):
	"""Social Networks Analysis Data Examples

	Data from Wasserman & Faust (1999) "Social Network Analysis"
	"""
	
	bioc = "SNAData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/SNAData_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/SNAData/SNAData_1.48.0.tar.gz"]

	version("1.48.0", md5="bfbd447afa550db44aa1db55e227cc10")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))

	# experiment
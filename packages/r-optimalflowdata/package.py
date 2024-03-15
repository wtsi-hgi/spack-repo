# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimalflowdata(RPackage):
	"""optimalFlowData

	Data files used as examples and for testing of the software provided in the optimalFlow package.
	"""
	
	bioc = "optimalFlowData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/optimalFlowData_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/optimalFlowData/optimalFlowData_1.14.0.tar.gz"]

	version("1.14.0", md5="790ea8af88ecf90abafdef9a7c4abb08")

	depends_on("r@4:", type=("build", "run"))

	# experiment
# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMammaprintdata(RPackage):
	"""RGLists from the Glas and Buyse breast cancer studies

	Gene expression data for the two breast cancer cohorts published by Glas and Buyse in 2006. This cohorts were used to implement and validate the mammaPrint breast cancer test.
	"""
	
	homepage = "http://luigimarchionni.org/breastTSP.html"
	bioc = "mammaPrintData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/mammaPrintData_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/mammaPrintData/mammaPrintData_1.38.0.tar.gz"]

	version("1.38.0", md5="08b3249a36d5f165a933bfab5eb05a2a")

	depends_on("r@2.13:", type=("build", "run"))


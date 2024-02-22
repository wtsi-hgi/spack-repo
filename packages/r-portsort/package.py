# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPortsort(RPackage):
	"""Factor-Based Portfolio Sorts

	Designed to aid both academic researchers and asset managers in conducting factor based portfolio sorts.  
    Provides functionality to sort assets into portfolios for up to three factors via a conditional or unconditional sorting procedure.
	"""
	
	cran = "portsort" 

	version("0.1.0", md5="fa6ac53d01de0ecf801f5f0b7922ae5a")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))

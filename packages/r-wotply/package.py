# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWotply(RPackage):
	"""Plot Connectivity Between Cells from Different Time Points

	It shows the connections between selected clusters from the latest time point and the clusters from all the previous time points. The transition matrices between time point t and t+1 are obtained from Waddington-OT analysis <https://github.com/ScialdoneLab/WOTPLY>.
	"""
	
	cran = "WOTPLY" 

	version("0.1.0", md5="66edd0be8a9ae2de348af466ccc9f6df")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))

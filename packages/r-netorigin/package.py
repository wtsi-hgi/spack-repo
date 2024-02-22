# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetorigin(RPackage):
	"""Origin Estimation for Propagation Processes on Complex Networks

	Performs network-based source estimation. Different approaches are available: effective distance median, recursive backtracking, and centrality-based source estimation. Additionally, we provide public transportation network data as well as methods for data preparation, source estimation performance analysis and visualization.
	"""
	
	homepage = "https://netorigin.manitz.org/"
	cran = "NetOrigin" 

	version("1.1-6", md5="e899b8bbbc4d4768a45b167d55555343")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))

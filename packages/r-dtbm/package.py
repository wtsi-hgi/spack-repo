# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtbm(RPackage):
	"""Multi-Way Spherical Clustering via Degree-Corrected Tensor Block
Models

	Implement weighted higher-order initialization and angle-based iteration for multi-way spherical clustering under degree-corrected tensor block model. See reference Jiaxin Hu and Miaoyan Wang (2023) <doi:10.1109/TIT.2023.3239521>.
	"""
	
	cran = "dTBM" 

	version("3.0", md5="030a257802d60522f6873f94b254bfbc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-weightedcluster", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))

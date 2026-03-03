# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMocca(RPackage):
	"""Multi-Objective Optimization for Collecting Cluster Alternatives

	Provides methods to analyze cluster alternatives based on multi-objective optimization of cluster validation indices. For details see Kraus et al. (2011) <doi:10.1007/s00180-011-0244-6>.
	"""
	
	cran = "MOCCA" 

	version("1.4", md5="b2ad80a0632eda0ed998e008a7099fff")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-cclust", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))

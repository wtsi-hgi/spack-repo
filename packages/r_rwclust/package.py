# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwclust(RPackage):
	"""Random Walk Clustering on Weighted Graphs

	Implements the random walk clustering algorithm for weighted graphs as found in Harel and Koren (2001) <https://link.springer.com/chapter/10.1007/3-540-45294-X_3>. 
	"""
	
	cran = "Rwclust" 

	version("0.1.0", md5="d0103bcd382cf6a25c215886187c0b33")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

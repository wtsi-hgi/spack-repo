# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFnn(RPackage):
	"""Fast Nearest Neighbor Search Algorithms and Applications.

	Cover-tree and kd-tree fast k-nearest neighbor search algorithms and
	related applications including KNN classification, regression and
	information measures are implemented."""

	cran = "FNN"

	version("1.1.4", md5="556e18063f6b54ff3d3117c4d8360215")

	depends_on("r@4:", type=("build", "run"))

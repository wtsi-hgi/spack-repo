# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGapmap(RPackage):
	"""Drawing Gapped Cluster Heatmaps with 'ggplot2'

	The gap encodes the distance between clusters and improves
    interpretation of cluster heatmaps. The gaps can be of the same
    distance based on a height threshold to cut the dendrogram. Another
    option is to vary the size of gaps based on the distance between
    clusters.
	"""
	
	homepage = "https://github.com/evanbiederstedt/gapmap"
	cran = "gapmap" 

	version("1.0.0", md5="b14c7598d6fdbf8aa1c58a7754dc28c9")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))

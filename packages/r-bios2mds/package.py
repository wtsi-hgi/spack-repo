# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBios2mds(RPackage):
	"""From Biological Sequences to Multidimensional Scaling

	Utilities dedicated to the analysis of
        biological sequences by metric MultiDimensional Scaling with
        projection of supplementary data. It contains functions for
        reading multiple sequence alignment files, calculating distance
        matrices, performing metric multidimensional scaling and
        visualizing results.
	"""
	
	cran = "bios2mds" 

	version("1.2.3", md5="c0c6a065dc36da2404093e381d8325a7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-amap", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))

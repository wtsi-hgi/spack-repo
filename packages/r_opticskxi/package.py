# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpticskxi(RPackage):
	"""OPTICS K-Xi Density-Based Clustering

	Provides a novel density-based cluster extraction method, OPTICS k-Xi, and a framework to compare k-Xi models using distance-based metrics to investigate datasets with unknown number of clusters.
	"""
	
	cran = "opticskxi" 

	version("0.1", md5="a2391578d952c44d7d4bc87e93aaf783")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))

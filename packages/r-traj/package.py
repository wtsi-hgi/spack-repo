# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTraj(RPackage):
	"""Clustering of Functional Data Based on Measures of Change

	Implements the three-step procedure proposed by Leffondree et al. (2004) to identify clusters of individual longitudinal trajectories. The procedure involves (1) calculating a number of measures of change capturing various features of the trajectories; (2) using a Principal Component Analysis based dimension reduction algorithm to select a subset of measures and (3) using the K-means clustering algorithm to identify clusters of trajectories.
	"""
	
	homepage = "https://CRAN.R-project.org/package=traj"
	cran = "traj" 

	version("2.0.1", md5="0aae84093d2493e6d47decad08486a75")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))

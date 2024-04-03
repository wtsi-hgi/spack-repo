# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTraj(RPackage):
	"""Clustering of Functional Data Based on Measures of Change

	Implements a three-step procedure in the spirit of Leffondree et al. (2004) to identify clusters of individual longitudinal trajectories. The procedure involves (1) computing a number of "measures of change"" capturing various features of the trajectories; (2) using a Principal Component Analysis based dimension reduction algorithm to select a subset of measures and (3) using the k-means clustering algorithm to identify clusters of trajectories.
	"""
	
	homepage = "https://CRAN.R-project.org/package=traj"
	cran = "traj" 

	version("2.1.0", md5="85eb498d710e46ef30b1619fad274999")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))

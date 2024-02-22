# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterbootstrap(RPackage):
	"""Analyze Clustered Data with Generalized Linear Models using the
Cluster Bootstrap

	Provides functionality for the analysis of clustered data using the cluster bootstrap. 
	"""
	
	homepage = "https://github.com/mathijsdeen/ClusterBootstrap"
	cran = "ClusterBootstrap" 

	version("1.1.2", md5="9a713749e043d2f2e932ffcbc57c6bd1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))

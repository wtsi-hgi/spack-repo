# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterObeu(RPackage):
	"""Cluster Analysis 'OpenBudgets.eu'

	Estimate and return the needed parameters for visualisations designed for 'OpenBudgets' <http://openbudgets.eu/> data. Calculate cluster analysis measures in Budget data of municipalities across Europe, according to the 'OpenBudgets' data model. It involves a set of techniques and algorithms used to find and divide the data into groups of similar observations. Also, can be used generally to extract visualisation parameters convert them to 'JSON' format and use them as input in a different graphical interface.
	"""
	
	homepage = "https://github.com/okgreece/Cluster.OBeu"
	cran = "Cluster.OBeu" 

	version("1.2.3", md5="684a6b7b926c810ca3470b3584b60bb5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-clvalid", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

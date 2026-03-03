# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupcluster(RPackage):
	"""Supervised Cluster Analysis

	Clusters features under the assumption that each cluster has a
 random effect and there is an outcome variable that is related to the random 
 effects by a linear regression. In this way the cluster analysis is 
 ``supervised'' by the outcome variable. An alternate specification is that 
 features in each cluster have the same compound symmetric normal distribution, 
 and the conditional distribution of the outcome given the features
 has the same coefficient for each feature in a cluster. 
	"""
	
	cran = "supcluster" 

	version("1.0.1", md5="365cfab4c6c5b3bcbb3783f9402fe7fd")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCstab(RPackage):
	"""Selection of Number of Clusters via Normalized Clustering
Instability

	Selection of the number of clusters in cluster analysis using
    stability methods.
	"""
	
	cran = "cstab" 

	version("0.2-2", md5="fae972cc0779563198893787e0ebeb9f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))

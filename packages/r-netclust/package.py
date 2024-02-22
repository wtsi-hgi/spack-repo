# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetclust(RPackage):
	"""Model-Based Clustering of Network Data

	Clustering unilayer and multilayer network data by means of finite mixtures is the main utility of 'netClust'.
	"""
	
	cran = "netClust" 

	version("1.0.1", md5="ee79de6c9fd8be5d427dd4027d78feed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

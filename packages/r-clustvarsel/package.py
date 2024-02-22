# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustvarsel(RPackage):
	"""Variable Selection for Gaussian Model-Based Clustering

	Variable selection for Gaussian model-based clustering as implemented in the 'mclust' package. The methodology allows to find the (locally) optimal subset of variables in a data set that have group/cluster information. A greedy or headlong search can be used, either in a forward-backward or backward-forward direction, with or without sub-sampling at the hierarchical clustering stage for starting 'mclust' models. By default the algorithm uses a sequential search, but parallelisation is also available.
	"""
	
	cran = "clustvarsel" 

	version("2.3.4", md5="688bd722ac4e4251ae4b2bc12e881bfd")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mclust@5.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-bma@3.18:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))

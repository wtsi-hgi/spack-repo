# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoxplotcluster(RPackage):
	"""Clustering Method Based on Boxplot Statistics

	Following Arroyo-Maté-Roque (2006), the function calculates the distance between rows or columns of the dataset using the generalized Minkowski metric as described by Ichino-Yaguchi (1994). The distance measure gives more weight to differences between quartiles than to differences between extremes, making it less sensitive to outliers. Further,the function calculates the silhouette width (Rousseeuw 1987) for different numbers of clusters and selects the number of clusters that maximizes the average silhouette width, unless a specific number of clusters is provided by the user. The approach implemented in this package is based on the following publications: Rousseeuw (1987) <doi:10.1016/0377-0427(87)90125-7>; Ichino-Yaguchi (1994) <doi:10.1109/21.286391>; Arroyo-Maté-Roque (2006) <doi:10.1007/3-540-34416-0_7>.
	"""
	
	cran = "boxplotcluster" 

	version("0.3", md5="ba43441f8b4c8fdb40181d0a5a960b65")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cluster@2.1.4:", type=("build", "run"))

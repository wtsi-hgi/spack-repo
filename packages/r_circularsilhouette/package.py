# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircularsilhouette(RPackage):
	"""Fast Silhouette on Circular or Linear Data Clusters

	Calculating silhouette information for clusters on
 circular or linear data using fast algorithms. These algorithms run in
 linear time on sorted data, in contrast to quadratic time by the
 definition of silhouette. When used together with the fast and optimal
 circular clustering method FOCC (Debnath & Song 2021)
 <doi:10.1109/TCBB.2021.3077573> implemented in R package 'OptCirClust',
 circular silhouette can be maximized to find the optimal number of
 circular clusters; it can also be used to estimate the period of noisy
 periodical data.
	"""
	
	cran = "CircularSilhouette" 

	version("0.0.1", md5="914a15488804850567b50a75040e376c")

	depends_on("r-optcirclust", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))

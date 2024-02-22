# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMajkmeans(RPackage):
	"""k-Means Algorithm with a Majorization-Minimization Method

	A hybrid of the K-means algorithm and a Majorization-Minimization method to introduce a robust clustering. The reference paper is: Julien Mairal, (2015) <doi:10.1137/140957639>. The two most important functions in package 'MajKMeans' are cluster_km() and cluster_MajKm(). cluster_km() clusters data without Majorization-Minimization and cluster_MajKm() clusters data with Majorization-Minimization method. Both of these functions calculate the sum of squares (SS) of clustering.
	"""
	
	cran = "MajKMeans" 

	version("0.1.0", md5="3b66f9bc0378bc7bef313ff7fbe1069c")

	depends_on("r-mass", type=("build", "run"))

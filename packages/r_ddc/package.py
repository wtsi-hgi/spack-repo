# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdc(RPackage):
	"""Distance Density Clustering Algorithm

	A distance density clustering (DDC) algorithm in R. DDC uses dynamic time warping (DTW) to compute a similarity matrix, based on which cluster centers and cluster assignments are found. DDC inherits dynamic time warping (DTW) arguments and constraints. The cluster centers are centroid points that are calculated using the DTW Barycenter Averaging (DBA) algorithm. The clustering process is divisive. At each iteration, cluster centers are updated and data is reassigned to cluster centers. Early stopping is possible. The output includes cluster centers and clustering assignment, as described in the paper (Ma et al (2017) <doi:10.1109/ICDMW.2017.11>).
	"""
	
	cran = "ddc" 

	version("1.0.1", md5="3de9ce177ef7e0935e618b5fbf9b9ea1")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dtw@1.22:", type=("build", "run"))
	depends_on("r-dtwclust@5.5:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))

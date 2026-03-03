# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKpeaks(RPackage):
	"""Determination of K Using Peak Counts of Features for Clustering

	The number of clusters (k) is needed to start all the partitioning clustering algorithms. An optimal value of this input argument is widely determined by using some internal validity indices. Since most of the existing internal indices suggest a k value which is computed from the clustering results after several runs of a clustering algorithm they are computationally expensive. On the contrary,  the package 'kpeaks' enables to estimate k before running any clustering algorithm. It is based on a simple novel technique using the descriptive statistics of peak counts of the features in a data set.
	"""
	
	cran = "kpeaks" 

	version("1.1.0", md5="67d7b4b6122fd5229bce53c96e8d47a2")

	depends_on("r@3.3:", type=("build", "run"))

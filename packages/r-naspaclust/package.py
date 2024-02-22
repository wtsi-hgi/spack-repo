# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaspaclust(RPackage):
	"""Nature-Inspired Spatial Clustering

	Implement and enhance the performance of spatial fuzzy clustering using Fuzzy Geographically Weighted Clustering with various optimization algorithms, mainly from Xin She Yang (2014) <ISBN:9780124167438> with book entitled Nature-Inspired Optimization Algorithms. The optimization algorithm is useful to tackle the disadvantages of clustering inconsistency when using the traditional approach. The distance measurements option is also provided in order to increase the quality of clustering results. The Fuzzy Geographically Weighted Clustering with nature inspired optimisation algorithm was firstly developed by Arie Wahyu Wijayanto and Ayu Purwarianti (2014) <doi:10.1109/CITSM.2014.7042178> using Artificial Bee Colony algorithm.
	"""
	
	cran = "naspaclust" 

	version("0.2.1", md5="2e969d4a6f4a485defb83c882425db96")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rdist", type=("build", "run"))
	depends_on("r-stabledist", type=("build", "run"))
	depends_on("r-beepr", type=("build", "run"))

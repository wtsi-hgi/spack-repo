# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastmit(RPackage):
	"""Fast Mutual Information Based Independence Test

	A mutual information estimator based on k-nearest neighbor method proposed by A. Kraskov, et al. (2004) <doi:10.1103/PhysRevE.69.066138> to measure general dependence and the time complexity for our estimator is only squared to the sample size, which is faster than other statistics. Besides, an implementation of mutual information based independence test is provided for analyzing multivariate data in Euclidean space (T B. Berrett, et al. (2019) <doi:10.1093/biomet/asz024>); furthermore, we extend it to tackle datasets in metric spaces.
	"""
	
	cran = "fastmit" 

	version("0.1.1", md5="11821608afd9f5b19e587642545d9a0a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))

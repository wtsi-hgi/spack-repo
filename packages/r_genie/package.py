# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenie(RPackage):
	"""Fast, Robust, and Outlier Resistant Hierarchical Clustering

	Includes the reference implementation of Genie - a hierarchical
    clustering algorithm that links two point groups in such a way that
    an inequity measure (namely, the Gini index) of the cluster sizes
    does not significantly increase above a given threshold.
    This method most often outperforms many other data segmentation approaches
    in terms of clustering quality as tested on a wide range of benchmark
    datasets. At the same time, Genie retains the high speed of the single
    linkage approach, therefore it is also suitable for analysing larger data sets.
    For more details see (Gagolewski et al. 2016 <DOI:10.1016/j.ins.2016.05.003>).
    For an even faster and more feature-rich implementation, including,
    amongst others, noise point detection, see the 'genieclust' package.
	"""
	
	homepage = "http://genieclust.gagolewski.com/"
	cran = "genie" 

	version("1.0.5", md5="187bf50eca2c33f3c2788cba31e229e0")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-genieclust", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))

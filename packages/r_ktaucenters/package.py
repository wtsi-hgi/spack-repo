# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKtaucenters(RPackage):
	"""Robust Clustering Procedures

	A clustering algorithm similar to K-Means is implemented, it has two main advantages, 
    namely (a) The estimator is resistant to outliers, that means that results of estimator are still correct when
    there are atypical values in the sample and (b) The estimator is efficient, roughly speaking, 
    if there are no outliers in the sample, results will be similar to those obtained by a classic algorithm (K-Means).
    Clustering procedure is carried out by minimizing the overall robust scale so-called tau scale.
    (see Gonzalez, Yohai and Zamar (2019) <arxiv:1906.08198>).
	"""
	
	cran = "ktaucenters" 

	version("1.0.0", md5="00ac4e3740d1f2191445137a6a5b4c63")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gse", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

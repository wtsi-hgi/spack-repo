# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcem(RPackage):
	"""Clustering Big Data using Expectation Maximization Star (EM*)
Algorithm

	Implements the Improved Expectation Maximisation EM* and the traditional EM algorithm for clustering 
    big data (gaussian mixture models for both multivariate and univariate datasets). This version 
    implements the faster alternative-EM* that expedites convergence via structure based data segregation. 
    The implementation supports both random and K-means++ based initialization. Reference: Parichit Sharma, 
    Hasan Kurban, Mehmet Dalkilic (2022) <doi:10.1016/j.softx.2021.100944>. Hasan Kurban, 
    Mark Jenne, Mehmet Dalkilic (2016) <doi:10.1007/s41060-017-0062-1>.
	"""
	
	homepage = "https://github.com/parichit/DCEM"
	cran = "DCEM" 

	version("2.0.5", md5="4be86f93577b7717b370b8f6ac8cf0d6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.7:", type=("build", "run"))
	depends_on("r-matrixcalc@1.0.3:", type=("build", "run"))
	depends_on("r-mass@7.3.49:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

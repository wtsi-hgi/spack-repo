# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnpac(RPackage):
	"""Non-Parametric Cluster Significance Testing with Reference to a
Unimodal Null Distribution

	Assess the significance of identified clusters and estimates the true number of clusters by comparing the explained variation due to the clustering from the original data to that produced by clustering a unimodal reference distribution which preserves the covariance structure in the data. The reference distribution is generated using kernel density estimation and a Gaussian copula framework. A dimension reduction strategy and sparse covariance estimation optimize this method for the high-dimensional, low-sample size setting. This method is described in Helgeson, Vock, and Bair (2021) <doi:10.1111/biom.13376>.
	"""
	
	cran = "UNPaC" 

	version("1.1.1", md5="7b517fb653c2cf427133d0e877f7321f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-huge", type=("build", "run"))
	depends_on("r-pdsce", type=("build", "run"))

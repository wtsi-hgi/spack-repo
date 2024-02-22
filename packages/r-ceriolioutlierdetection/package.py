# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCeriolioutlierdetection(RPackage):
	"""Outlier Detection Using the Iterated RMCD Method of Cerioli
(2010)

	Implements the iterated RMCD method of Cerioli (2010)
	for multivariate outlier detection via robust Mahalanobis distances. Also
	provides the finite-sample RMCD method discussed in the paper, as well as 
	the methods provided in Hardin and Rocke (2005) <doi:10.1198/106186005X77685> 
	and Green and Martin (2017).
	"""
	
	homepage = "https://christopherggreen.github.io/CerioliOutlierDetection/"
	cran = "CerioliOutlierDetection" 

	version("1.1.13", md5="8ed31224a79f3f3416f5ce13f077bd97")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-robustbase@0.91.1:", type=("build", "run"))

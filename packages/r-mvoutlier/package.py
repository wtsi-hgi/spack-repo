# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvoutlier(RPackage):
	"""Multivariate Outlier Detection Based on Robust Methods

	Various methods for multivariate outlier detection: arw, a Mahalanobis-type method with an adaptive outlier cutoff value; locout, a method incorporating local neighborhood; pcout, a method for high-dimensional data; mvoutlier.CoDa, a method for compositional data. References are provided in the corresponding help files.
	"""
	
	homepage = "http://cstat.tuwien.ac.at/filz/"
	cran = "mvoutlier" 

	version("2.1.1", md5="ccac1acc18ba4a0e0be6773c497ef16f")

	depends_on("r-sgeostat", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKbmvtskew(RPackage):
	"""Khattree-Bahuguna's Univariate and Multivariate Skewness

	Computes Khattree-Bahuguna's univariate and multivariate skewness, principal-component-based Khattree-Bahuguna's multivariate skewness. It also provides several measures of univariate or multivariate skewnesses including, Pearson’s coefficient of skewness, Bowley’s univariate skewness and Mardia's multivariate skewness. See Khattree, R. and Bahuguna, M. (2019) <doi: 10.1007/s41060-018-0106-1>.
	"""
	
	cran = "KbMvtSkew" 

	version("1.0.2", md5="b43023540aed43765f4e9ba57a4f5711")

	depends_on("r@3.6:", type=("build", "run"))

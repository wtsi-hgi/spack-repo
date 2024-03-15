# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCocorresp(RPackage):
	"""Co-Correspondence Analysis Methods

	Fits predictive and symmetric co-correspondence analysis (CoCA) models to relate one data matrix to another data matrix. More specifically, CoCA maximises the weighted covariance between the weighted averaged species scores of one community and the weighted averaged species scores of another community. CoCA attempts to find patterns that are common to both communities.
	"""
	
	homepage = "https://gavinsimpson.github.io/cocorresp/"
	cran = "cocorresp" 

	version("0.4-4", md5="b512b4119213ab5e131bc4063added66")

	depends_on("r-vegan@2.5.0:", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))

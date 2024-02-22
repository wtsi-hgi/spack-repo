# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGustave(RPackage):
	"""A User-Oriented Statistical Toolkit for Analytical Variance
Estimation

	Provides a toolkit for analytical variance estimation in survey sampling. Apart from the implementation of standard variance estimators, its main feature is to help the sampling expert produce easy-to-use variance estimation "wrappers", where systematic operations (linearization, domain estimation) are handled in a consistent and transparent way.
	"""
	
	homepage = "https://github.com/InseeFr/gustave"
	cran = "gustave" 

	version("1.0.0", md5="bfda18d6a3f426a9942b4de93ea198c1")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

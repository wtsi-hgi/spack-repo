# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpboost(RPackage):
	"""Combining Tree-Boosting with Gaussian Process and Mixed Effects
Models

	An R package that allows for combining tree-boosting with Gaussian process and mixed effects models. It also allows for independently doing tree-boosting as well as inference and prediction for Gaussian process and mixed effects models. See <https://github.com/fabsig/GPBoost> for more information on the software and Sigrist (2022, JMLR) <https://www.jmlr.org/papers/v23/20-322.html> and Sigrist (2023, TPAMI) <doi:10.1109/TPAMI.2022.3168152> for more information on the methodology.
	"""
	
	homepage = "https://github.com/fabsig/GPBoost"
	cran = "gpboost" 

	version("1.2.9", md5="27b63adaa49dcdfd7f7c43f3d97f9608")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6@2:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-matrix@1.1.0:", type=("build", "run"))

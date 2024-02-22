# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinsegbstrap(RPackage):
	"""Piecewise Smooth Regression by Bootstrapped Binary Segmentation

	Provides methods for piecewise smooth regression. A piecewise smooth signal is estimated by applying a bootstrapped test recursively (binary segmentation approach). Each bootstrapped test decides whether the underlying signal is smooth on the currently considered subsegment or contains at least one further change-point.
	"""
	
	cran = "BinSegBstrap" 

	version("1.0-1", md5="aa637cb339e2507c660b86bedf2e702a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))

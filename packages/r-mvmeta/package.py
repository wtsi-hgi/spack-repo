# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvmeta(RPackage):
	"""Multivariate and Univariate Meta-Analysis and Meta-Regression

	Collection of functions to perform fixed and random-effects multivariate and univariate meta-analysis and meta-regression.
	"""
	
	homepage = "http://www.ag-myresearch.com/package-mvmeta"
	cran = "mvmeta" 

	version("1.0.3", md5="be535e00357e1ffec02dcefac4cb5146")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-mixmeta", type=("build", "run"))

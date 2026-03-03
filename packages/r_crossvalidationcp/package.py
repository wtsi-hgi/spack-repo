# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrossvalidationcp(RPackage):
	"""Cross-Validation for Change-Point Regression

	Implements the cross-validation methodology from Pein and Shah (2021) <arXiv:2112.03220>. Can be customised by providing different cross-validation criteria, estimators for the change-point locations and local parameters, and freely chosen folds. Pre-implemented estimators and criteria are available. It also includes our own implementation of the COPPS procedure <doi:10.1214/19-AOS1814>.
	"""
	
	cran = "crossvalidationCP" 

	version("1.1", md5="7d6b03133e7fcec59b0c144da20bf2cd")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-changepoint@2:", type=("build", "run"))
	depends_on("r-fpopw@1.1:", type=("build", "run"))
	depends_on("r-wbs@1.4:", type=("build", "run"))

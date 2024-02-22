# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGbmt(RPackage):
	"""Group-Based Multivariate Trajectory Modeling

	Estimation and analysis of group-based multivariate trajectory models (Nagin, 2018 <doi:10.1177/0962280216673085>; Magrini, 2022 <doi:10.1007/s10182-022-00437-9>). The package implements an Expectation-Maximization (EM) algorithm allowing unbalanced panel and missing values, and provides several functionalities for prediction and graphical representation.
	"""
	
	cran = "gbmt" 

	version("0.1.3", md5="30f75bd49ca8d2825a07b154405e01ae")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

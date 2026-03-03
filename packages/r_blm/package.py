# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlm(RPackage):
	"""Binomial Linear Regression

	Implements regression models for binary data on the absolute risk scale. These models are applicable to cohort and population-based case-control data.
	"""
	
	cran = "blm" 

	version("2022.0.0.1", md5="a8759e8b70f78e691210f854d8385452")

	depends_on("r@3:", type=("build", "run"))

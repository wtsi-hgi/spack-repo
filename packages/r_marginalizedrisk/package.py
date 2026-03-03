# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarginalizedrisk(RPackage):
	"""Estimating Marginalized Risk

	Estimates risk as a function of a marker by integrating over other covariates in a conditional risk model.
	"""
	
	cran = "marginalizedRisk" 

	version("2024.1-27", md5="d7dd50b6a2ae113d1964e3c7c2c6a518")

	depends_on("r@4:", type=("build", "run"))

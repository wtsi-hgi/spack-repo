# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdsce(RPackage):
	"""Positive Definite Sparse Covariance Estimators

	Compute and tune some positive definite and sparse covariance
  estimators.
	"""
	
	cran = "PDSCE" 

	version("1.2.1", md5="d660fbcdbf7c050b282dfe4e7f5ebf49")

	depends_on("r@2.10:", type=("build", "run"))

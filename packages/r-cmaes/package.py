# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmaes(RPackage):
	"""Covariance Matrix Adapting Evolutionary Strategy

	Single objective optimization using a CMA-ES.
	"""
	
	cran = "cmaes" 

	version("1.0-12", md5="5ef1a745a0ba03edd416b7ddb3728611")

	depends_on("r@2.9:", type=("build", "run"))

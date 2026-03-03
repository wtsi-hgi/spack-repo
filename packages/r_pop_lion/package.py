# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopLion(RPackage):
	"""Models for Simulating Lion Populations

	Simulate the dynamic of lion populations using a specific Individual-Based Model (IBM) compiled in C.
	"""
	
	cran = "pop.lion" 

	version("1.0.1", md5="9b926850f3432be0c5fd7a13d60be192")

	depends_on("r-abind", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))

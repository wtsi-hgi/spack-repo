# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpa(RPackage):
	"""Confirmatory Path Analysis Through 'd-sep' Tests

	Functions to test and compare causal models using Confirmatory Path Analysis. 
	"""
	
	cran = "cpa" 

	version("1.0.1", md5="d6e6d88a19866a4c4ad954c00762a1af")

	depends_on("r@3.2:", type=("build", "run"))

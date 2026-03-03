# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactoptd(RPackage):
	"""Factorial Optimal Designs for Two-Colour cDNA Microarray
Experiments

	Computes factorial A-, D- and E-optimal designs for two-colour cDNA microarray experiments.
	"""
	
	cran = "factoptd" 

	version("1.0.3", md5="1631003aaef9f9e4a97ef61005b9cd80")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))

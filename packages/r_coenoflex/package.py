# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoenoflex(RPackage):
	"""Gradient-Based Coenospace Vegetation Simulator

	Simulates the composition of samples of vegetation
        according to gradient-based vegetation theory.  Features a
        flexible algorithm incorporating competition and complex
        multi-gradient interaction.
	"""
	
	cran = "coenoflex" 

	version("2.2-0", md5="d1e57e46d035fa8ff6292c86a9ea548d")

	depends_on("r-mgcv", type=("build", "run"))

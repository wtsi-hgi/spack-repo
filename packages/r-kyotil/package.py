# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKyotil(RPackage):
	"""Utility Functions for Statistical Analysis Report Generation and
Monte Carlo Studies

	Helper functions for creating formatted summary of regression models, writing publication-ready tables to latex files, and running Monte Carlo experiments.
	"""
	
	cran = "kyotil" 

	version("2024.1-30", md5="a6700c0ba66135deef335abbad1ed330")

	depends_on("r@3.6:", type=("build", "run"))

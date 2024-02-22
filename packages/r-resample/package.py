# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResample(RPackage):
	"""Resampling Functions

	Bootstrap, permutation tests, and jackknife,
	featuring easy-to-use syntax.
	"""
	
	cran = "resample" 

	version("0.6", md5="e8d3f0dd5ec1da48bc8ef7220a4d2e53")

	depends_on("r@3.1:", type=("build", "run"))

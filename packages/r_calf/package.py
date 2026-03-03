# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalf(RPackage):
	"""Coarse Approximation Linear Function

	Contains greedy algorithms for coarse approximation linear functions.
	"""
	
	cran = "CALF" 

	version("1.0.17", md5="3f5f10f985f198f0cc4002f67a8d9687")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

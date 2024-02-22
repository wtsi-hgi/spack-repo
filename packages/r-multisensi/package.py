# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultisensi(RPackage):
	"""Multivariate Sensitivity Analysis

	Functions to perform sensitivity analysis on a model with multivariate output.
	"""
	
	cran = "multisensi" 

	version("2.1-1", md5="ec3ac096db5f7d65bd671de39fa6b777")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-sensitivity", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))

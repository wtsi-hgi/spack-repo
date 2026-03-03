# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHett(RPackage):
	"""Heteroscedastic t-Regression

	Functions for the fitting and summarizing of heteroscedastic t-regression.
	"""
	
	cran = "hett" 

	version("0.3-3", md5="0f42646be744c4fed80ef7d9b6fa4e1b")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))

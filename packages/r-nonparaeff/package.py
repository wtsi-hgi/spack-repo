# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonparaeff(RPackage):
	"""Nonparametric Methods for Measuring Efficiency and Productivity

	Efficiency and productivity indices are measured using this package. This package contains functions for measuring efficiency and productivity of decision making units (DMUs) under the framework of Data Envelopment Analysis (DEA) and its variations.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "nonparaeff" 

	version("0.5-13", md5="9d259009a8600c2e01fb81e41dc0a8cc")

	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))

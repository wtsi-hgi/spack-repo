# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMargins(RPackage):
	"""Marginal Effects for Model Objects

	An R port of Stata's 'margins' command, which can be used to
    calculate marginal (or partial) effects from model objects.
	"""
	
	homepage = "https://github.com/leeper/margins"
	cran = "margins" 

	version("0.3.26", md5="089978cd9b7fd9b0ba75525c9efe4641")

	depends_on("r-prediction@0.3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))

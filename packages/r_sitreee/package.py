# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSitreee(RPackage):
	"""Sitree Extensions

	Provides extensions for package 'sitree' for allometric variables, growth, mortality, recruitment, management, tree removal and external modifiers functions.
	"""
	
	cran = "sitreeE" 

	version("0.0-8", md5="2bcabb6714edbfeeb762de774b92ad1a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-sitree", type=("build", "run"))

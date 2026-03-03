# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIfatools(RPackage):
	"""Toolkit for Item Factor Analysis with 'OpenMx'

	Tools, tutorials, and demos of Item Factor Analysis using 'OpenMx'.
    This software is described in Pritikin & Falk (2020) <doi:10.1177/0146621620929431>.
	"""
	
	homepage = "https://github.com/jpritikin/ifaTools"
	cran = "ifaTools" 

	version("0.23", md5="c5d559110ed868d0185351062a21162b")

	depends_on("r-shiny@0.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rpf@0.48:", type=("build", "run"))
	depends_on("r-openmx@2.3.1:", type=("build", "run"))
	depends_on("r@2.14:", type=("build", "run"))

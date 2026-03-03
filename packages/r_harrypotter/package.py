# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarrypotter(RPackage):
	"""Palettes Generated from All "Harry Potter" Movies

	Implementation of characteristic palettes inspired in the Wizarding World and the Harry Potter movie franchise.
	"""
	
	homepage = "https://github.com/aljrico/harrypotter"
	cran = "harrypotter" 

	version("2.1.1", md5="f032c91d396ce69e965431316883473d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))

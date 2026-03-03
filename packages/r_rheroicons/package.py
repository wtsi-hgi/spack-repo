# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRheroicons(RPackage):
	"""A Zero Dependency 'SVG' Icon Library for 'Shiny'

	An implementation of the 'Heroicons' icon library for 'shiny'
    applications and other 'R' web-based projects. You can search, render,
    and customize icons without 'CSS' or 'JavaScript' dependencies.
	"""
	
	cran = "rheroicons" 

	version("1.0.0", md5="b788fa4dabb164bc84f894662c791932")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmltools@0.5.3:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))

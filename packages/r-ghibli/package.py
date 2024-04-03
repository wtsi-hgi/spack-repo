# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGhibli(RPackage):
	"""Studio Ghibli Colour Palettes

	Colour palettes inspired by Studio Ghibli <https://en.wikipedia.org/wiki/Studio_Ghibli> 
    films, ported to R for your enjoyment.
	"""
	
	homepage = "https://ewenme.github.io/ghibli/"
	cran = "ghibli" 

	version("0.3.4", md5="e7da1eb7a5ee03ef8c08aae4ff192b8b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-prismatic", type=("build", "run"))

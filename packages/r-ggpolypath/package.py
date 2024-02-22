# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpolypath(RPackage):
	"""Polygons with Holes for the Grammar of Graphics

	Tools for working with polygons with holes in 'ggplot2', with a
    new 'geom' for drawing a 'polypath' applying the 'evenodd' or 'winding'
    rules.
	"""
	
	homepage = "https://mdsumner.github.io/ggpolypath/"
	cran = "ggpolypath" 

	version("0.3.0", md5="42b10bc86671071262cac118a2314e31")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))

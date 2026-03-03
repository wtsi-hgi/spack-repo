# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiscale(RPackage):
	"""Tools and Palettes for Bivariate Thematic Mapping

	Provides a 'ggplot2' centric approach to bivariate mapping. This is a 
    technique that maps two quantities simultaneously rather than the single value 
    that most thematic maps display. The package provides a suite of tools 
    for calculating breaks using multiple different approaches, a selection of 
    palettes appropriate for bivariate mapping and scale functions for 'ggplot2' 
    calls that adds those palettes to maps. Tools for creating bivariate legends 
    are also included.
	"""
	
	homepage = "https://chris-prener.github.io/biscale/"
	cran = "biscale" 

	version("1.0.0", md5="f039f97946a722604fdfddc26230283f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-classint", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

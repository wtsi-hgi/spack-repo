# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSanzo(RPackage):
	"""Color Palettes Based on the Works of Sanzo Wada

	Inspired by the art and color research of Sanzo Wada (1883-1967), 
    his "Dictionary Of Color Combinations" (2011, ISBN:978-4861522475), and the 
    interactive site by Dain M. Blodorn Kim <https://github.com/dblodorn/sanzo-wada>, 
    this package brings Wada's color combinations to R for easy use in data 
    visualizations. This package honors 60 of Wada's color combinations: 
    20 duos, 20 trios, and 20 quads.
	"""
	
	homepage = "https://github.com/jmaasch/sanzo"
	cran = "sanzo" 

	version("0.1.0", md5="eb7c373881d575a27c9e16d620f14b1a")


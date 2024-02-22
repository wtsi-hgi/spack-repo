# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPals(RPackage):
	"""Color Palettes, Colormaps, and Tools to Evaluate Them

	A comprehensive collection of color palettes, colormaps, and tools to evaluate them.
	"""
	
	homepage = "https://kwstat.github.io/pals/"
	cran = "pals" 

	version("1.8", md5="fc8f770432f8b1f7a7b35200640c828f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dichromat", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-mapproj", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKaradacolor(RPackage):
	"""Color Palettes Inspired by Japanese Landscape and Culture

	The palette includes motifs from Japanese landscape and culture.
    And it provides commands for color manipulation and 'ggplot2' color scales.
	"""
	
	homepage = "https://github.com/KaradaGood/KaradaColor"
	cran = "KaradaColor" 

	version("0.1.5", md5="d91b1da2e104b86721a520f31d897319")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

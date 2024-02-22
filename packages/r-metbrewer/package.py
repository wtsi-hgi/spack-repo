# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetbrewer(RPackage):
	"""Color Palettes Inspired by Works at the Metropolitan Museum of
Art

	Palettes Inspired by Works at the Metropolitan Museum of Art in New York. Currently contains over 50 color schemes and checks for colorblind-friendliness of palettes. Colorblind accessibility checked using the '{colorblindcheck} package by Jakub Nowosad'<https://jakubnowosad.com/colorblindcheck/>.
	"""
	
	cran = "MetBrewer" 

	version("0.2.0", md5="6345d9abcd277300725268803d684ed5")

	depends_on("r-ggplot2", type=("build", "run"))

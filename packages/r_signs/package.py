# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigns(RPackage):
	"""Insert Proper Minus Signs

	Provides convenience functions to replace hyphen-minuses (ASCII 45)
    with proper minus signs (Unicode character 2212). The true minus matches
    the plus symbol in width, line thickness, and height above the baseline.
    It was designed for mathematics, looks better in presentation,
    and is understood properly by screen readers.
	"""
	
	homepage = "https://benjaminwolfe.github.io/signs"
	cran = "signs" 

	version("0.1.2", md5="3c5b4975474193ddfbee169ae47d8948")

	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))

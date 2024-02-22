# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVangogh(RPackage):
	"""A Vincent Van Gogh Color Palette Generator

	Palettes generated from Vincent van Gogh's paintings.
	"""
	
	homepage = "https://github.com/cherylisabella/vangogh"
	cran = "vangogh" 

	version("0.1.1", md5="8877b2299395ec448f35a9f2c9559a06")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))

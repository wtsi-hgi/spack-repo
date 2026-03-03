# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmsvg(RPackage):
	"""Build and Transform 'SVG' Objects

	Build 'SVG' components using element-based functions. With
    an 'svg' object, we can modify its graphical elements with a suite of
    transform functions.
	"""
	
	homepage = "https://github.com/rich-iannone/omsvg"
	cran = "omsvg" 

	version("0.1.0", md5="cfe2a6aef30c556242f548e46536586f")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.3:", type=("build", "run"))
	depends_on("r-gt@0.2.2:", type=("build", "run"))
	depends_on("r-htmltools@0.5.1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
	depends_on("r-sass@0.3:", type=("build", "run"))
	depends_on("r-xml2@1.3.2:", type=("build", "run"))

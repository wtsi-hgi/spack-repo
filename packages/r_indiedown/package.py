# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndiedown(RPackage):
	"""Individual R Markdown Templates

	Simplifies the generation of customized R Markdown PDF templates.
    A template may include an individual logo, typography, geometry or color
    scheme. The package provides a skeleton with detailed instructions for
    customizations. The skeleton can be modified by changing defaults in the
    'YAML' header, by adding additional 'LaTeX' commands or by applying dynamic
    adjustments in R. Individual corporate design elements, such as a title page, can be added as R functions that produce 'LaTeX' code.
	"""
	
	homepage = "https://cynkra.github.io/indiedown/"
	cran = "indiedown" 

	version("0.1.1", md5="2d0751c254e261454f65a4a330a5c8ca")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-gfonts", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))

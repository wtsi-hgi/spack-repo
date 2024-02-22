# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhosphoricons(RPackage):
	"""'Phosphor' Icons for R

	Use 'Phosphor' icons in 'shiny' applications or 'rmarkdown' documents. Icons are available in
    5 different weights and can be customized by setting color, size, orientation and more.
	"""
	
	homepage = "https://dreamrs.github.io/phosphoricons/"
	cran = "phosphoricons" 

	version("0.2.0", md5="09548bc169c57b0d37f2bdacd6c425cc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmltools@0.3:", type=("build", "run"))

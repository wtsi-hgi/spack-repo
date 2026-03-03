# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdthemes(RPackage):
	"""Markdown Themes for 'ggplot2'

	A collection of 'ggplot2' themes that render text as markdown/HTML. This enables
    the creation of complex formatted plot labels, e.g. titles with individual words highlighted
    in different colors.
	"""
	
	cran = "mdthemes" 

	version("0.1.0", md5="f0f68cbb775af735255d2db5d5e9a7a6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-hrbrthemes", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-tvthemes", type=("build", "run"))

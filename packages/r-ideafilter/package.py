# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdeafilter(RPackage):
	"""Agnostic, Idiomatic Data Filter Module for Shiny

	When added to an existing shiny app, users may subset any
    developer-chosen R data.frame on the fly. That is, users are empowered to
    slice & dice data by applying multiple (order specific) filters using the
    AND (&) operator between each, and getting real-time updates on the number
    of rows effected/available along the way. Thus, any downstream processes
    that leverage this data source (like tables, plots, or statistical procedures)
    will re-render after new filters are applied. The shiny module’s user interface has
    a 'minimalist' aesthetic so that the focus can be on the data &
    other visuals. In addition to returning a reactive (filtered) data.frame,
    'IDEAFilter' as also returns 'dplyr' filter statements used to actually slice
    the data.
	"""
	
	homepage = "https://biogen-inc.github.io/IDEAFilter/"
	cran = "IDEAFilter" 

	version("0.1.2", md5="d754ddf2550cb96099f5624e1db7e75f")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pillar@1.5:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-shinytime", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))

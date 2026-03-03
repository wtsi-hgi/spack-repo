# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPicker(RPackage):
	"""Pick Data Points from a Deck.gl Scatterplot

	Performant interactive scatterplot for ~ 1 million points. Zoom, pan,
    and pick points. Includes tooltips, labels, a grid overlay, legend, and
    coupled interactions across multiple plots.
	"""
	
	homepage = "https://github.com/hms-dbmi/picker"
	cran = "picker" 

	version("0.2.6", md5="4f579e11b67f847bc5a92fd0f6ff1481")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5.3:", type=("build", "run"))

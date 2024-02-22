# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVegawidget(RPackage):
	"""'Htmlwidget' for 'Vega' and 'Vega-Lite'

	'Vega' and 'Vega-Lite' parse text in 'JSON' notation to render 
  chart-specifications into 'HTML'. This package is used to facilitate the 
  rendering. It also provides a means to interact with signals, events,
  and datasets in a 'Vega' chart using 'JavaScript' or 'Shiny'.
	"""
	
	homepage = "https://vegawidget.github.io/vegawidget/"
	cran = "vegawidget" 

	version("0.5.0", md5="b065e806cfe74ba97c5879701b4f5b17")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))

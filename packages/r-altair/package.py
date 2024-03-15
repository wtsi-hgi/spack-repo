# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAltair(RPackage):
	"""Interface to 'Altair'

	Interface to 'Altair' <https://altair-viz.github.io>, which itself 
  is a 'Python' interface to 'Vega-Lite' <https://vega.github.io/vega-lite/>.
  This package uses the 'Reticulate' framework 
  <https://rstudio.github.io/reticulate/> to manage the interface between R
  and 'Python'.
	"""
	
	homepage = "https://github.com/vegawidget/altair"
	cran = "altair"

	version("4.2.3", md5="3af0f5b450b69a70521a6d32f497efae")

	depends_on("r-reticulate@1.23:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-vegawidget@0.4.1:", type=("build", "run"))
	depends_on("r-repr", type=("build", "run"))
	depends_on("py-altair", type=("build", "link", "run"))

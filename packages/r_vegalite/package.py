# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVegalite(RPackage):
	"""Tools to Encode Visualizations with the 'Grammar of
Graphics'-Like 'Vega-Lite' 'Spec'

	The 'Vega-Lite' 'JavaScript' framework provides a higher-level grammar
    for visual analysis, akin to 'ggplot' or 'Tableau', that generates complete 'Vega'
    specifications. Functions exist which enable building a valid 'spec' from scratch
    or importing a previously created 'spec' file. Functions also exist to export 'spec'
    files and to generate code which will enable plots to be embedded in properly
    configured web pages. The default behavior is to generate an 'htmlwidget'.
	"""
	
	homepage = "http://github.com/hrbrmstr/vegalite"
	cran = "vegalite" 

	version("0.6.1", md5="526fb97e36a3b4a7d3899ee8ea396a06")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-htmlwidgets@0.6:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("r-webshot", type=("build", "run"))
	depends_on("r-base64", type=("build", "run"))

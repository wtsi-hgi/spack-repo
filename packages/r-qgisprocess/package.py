# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQgisprocess(RPackage):
	"""Use 'QGIS' Processing Algorithms

	Provides seamless access to the 'QGIS'
    (<https://qgis.org/en/site/>) processing toolbox using the standalone
    'qgis_process' command-line utility.  Both native and third-party
    (plugin) processing providers are supported.  Beside referring data
    sources from file, also common objects from 'sf', 'terra' and 'stars'
    are supported. The native processing algorithms are documented by QGIS.org 
    (2023) <https://docs.qgis.org/latest/en/docs/user_manual/processing_algs/>.
	"""
	
	homepage = "https://r-spatial.github.io/qgisprocess/"
	cran = "qgisprocess" 

	version("0.3.0", md5="d3160217eca7fe5e01f54432335f6e23")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-processx@3.5.2:", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("qgis", type=("build", "link", "run"))

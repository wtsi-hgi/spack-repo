# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrowserviz(RPackage):
	"""BrowserViz: interactive R/browser graphics using websockets and JSON

	Interactvive graphics in a web browser from R, using websockets and JSON.
	"""
	
	homepage = "https://gladkia.github.io/BrowserViz/"
	bioc = "BrowserViz" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BrowserViz_2.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BrowserViz/BrowserViz_2.24.0.tar.gz"]

	version("2.30.0", tag="RELEASE_3_21")
	version("2.24.0", sha256="256fc9b97531f85a263f732bd2dc3144f1b22f4105e94a35b1d731e8fedd9cd4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-httpuv@1.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BrowserViz_2.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BrowserViz/BrowserViz_2.24.0.tar.gz"]

	version("2.24.0", md5="ae6366903bd754cbe0ca0d21168c6883")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-httpuv@1.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

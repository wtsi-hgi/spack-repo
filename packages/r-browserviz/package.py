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

	version("2.30.0", commit="a71a830f3fdf9ba83f19185066074d6c69d04213")
	version("2.24.0", commit="e825c9832e3c4b25515e1fd6b0707d46bbce39de")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-httpuv@1.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

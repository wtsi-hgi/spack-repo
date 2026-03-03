# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinytree(RPackage):
	"""jsTree Bindings for Shiny

	Exposes bindings to jsTree -- a JavaScript library
    that supports interactive trees -- to enable a rich, editable trees in
    Shiny.
	"""
	
	cran = "shinyTree" 

	version("0.3.1", md5="7c33eb07433f34747e937a70c94581c9")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-shiny@0.9:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-promises", type=("build", "run"))

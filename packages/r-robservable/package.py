# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobservable(RPackage):
	"""Import an Observable Notebook as HTML Widget

	Allows loading and displaying an Observable notebook (online JavaScript  
    notebooks powered by <https://observablehq.com>) as an HTML Widget in an R 
    session, 'shiny' application or 'rmarkdown' document.
	"""
	
	homepage = "https://juba.github.io/robservable/"
	cran = "robservable" 

	version("0.2.2", md5="488ec258295c86b69971efc8412e19fd")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))

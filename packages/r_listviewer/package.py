# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RListviewer(RPackage):
	"""'htmlwidget' for Interactive Views of R Lists

	R lists, especially nested lists, can be very difficult to
    visualize or represent. Sometimes 'str()' is not enough, so this suite of
    htmlwidgets is designed to help see, understand, and maybe even modify your R
    lists.  The function 'reactjson()' requires a package
    'reactR' that can be installed from CRAN or <https://github.com/timelyportfolio/reactR>.
	"""
	
	homepage = "https://github.com/timelyportfolio/listviewer"
	cran = "listviewer" 

	version("4.0.0", md5="07909f16effa110f98f803f137c61302")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))

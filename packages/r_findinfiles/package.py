# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFindinfiles(RPackage):
	"""Find Pattern in Files

	Creates a HTML widget which displays the results of searching for a pattern in files in a given folder. The results can be viewed in the 'RStudio' viewer pane, included in a 'R Markdown' document or in a 'Shiny' app. Also provides a 'Shiny' application allowing to run the widget and to navigate in the results.
	"""
	
	homepage = "https://github.com/stla/findInFiles"
	cran = "findInFiles" 

	version("0.4.0", md5="14e8ef1e5b49412ade45cb15eafe7c2c")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))

# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinytoastify(RPackage):
	"""Pretty Notifications for 'Shiny'

	This is a wrapper of the 'React' library 'React-Toastify'. It allows to show some notifications (toasts) in 'Shiny' applications. There are options for the style, the position, the transition effect, and more.
	"""
	
	homepage = "https://github.com/stla/shinyToastify"
	cran = "shinyToastify" 

	version("2.0.0", md5="61eacee93309f59ee6dad5c2803038f3")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-reactr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-fontawesome", type=("build", "run"))

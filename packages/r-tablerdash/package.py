# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTablerdash(RPackage):
	"""'Tabler' API for 'Shiny'

	'R' interface to the 'Tabler' HTML template. See more here <https://tabler.io>. 
    'tablerDash' is a light 'Bootstrap 4' dashboard template. There are different 
     layouts available such as a one page dashboard or a multi page template,
     where the navigation menu is contained in the navigation bar. A fancy example
     is available at <https://dgranjon.shinyapps.io/shinyMons/>.
	"""
	
	homepage = "https://rinterface.github.io/tablerDash/"
	cran = "tablerDash" 

	version("0.1.0", md5="83e5502845c1e8b2953fc23a6da162a0")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))

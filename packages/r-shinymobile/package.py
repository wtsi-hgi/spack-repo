# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinymobile(RPackage):
	"""Mobile Ready 'shiny' Apps with Standalone Capabilities

	Develop outstanding 'shiny' apps for 'iOS', 'Android', desktop as well as beautiful 'shiny' gadgets.
    'shinyMobile' is built on top of the latest 'Framework7' template <https://framework7.io>.
    Discover 14 new input widgets (sliders, vertical sliders, stepper, 
    grouped action buttons, toggles, picker, smart select, ...), 2 themes (light and dark), 
    12 new widgets (expandable cards, badges, chips, timelines, gauges, progress bars, ...) 
    combined with the power of server-side notifications such as alerts, modals, toasts,
    action sheets, sheets (and more) as well as 3 layouts (single, tabs and split).
	"""
	
	homepage = "https://github.com/RinteRface/shinyMobile"
	cran = "shinyMobile" 

	version("1.0.0", md5="a90da3731b4bb40e65499dab6ffda033")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
